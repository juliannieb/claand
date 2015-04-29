from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.db.models import Q

from principal.models import Vendedor
from empresas.models import Empresa
from contactos.models import Contacto


class VistasEmpresas(TestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    def setUp(self):
        grupo_vendedor = Group.objects.get_or_create(name="vendedor")[0]
        self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.vendedor = User.objects.create_user('julian', 'julian@abc.com', 'julian')
        self.vendedor.groups.add(grupo_vendedor)
    
    def tearDown(self):
        pass

    def test_empresas_usuario_no_autenticado(self):
        """ test para checar si un usuario no registrado es redirigido al login
        al intentar entrar a las vistas del app de empresas.
        """
        response = self.client.get(reverse('empresas:registrar_empresa'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('empresas:get_municipio'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('empresas:consultar_empresas'))
        self.assertEqual(response.status_code, 302)

    def test_vista_getmunicipio(self):
        """ test para probar si un usuario intenta acceder a la url empleada para
        el AJAX de get_municipio es redirigido al index.
        """
        login = self.client.login(username='temporary', password='temporary')
        self.assertTrue(login)
        response = self.client.get(reverse('empresas:get_municipio'))
        self.assertRedirects(response, reverse('principal:index'), status_code=302, target_status_code=200)

    def test_vista_empresa(self):
        """ Test para probar si al ver el detalle de una empresa, se muestra su informacion
        correspondiente
        """
        login = self.client.login(username='temporary', password='temporary')
        self.assertTrue(login)
        response = self.client.get(reverse('empresas:empresa', args=('claand',)))
        self.assertEqual(response.status_code, 200)
        empresa = Empresa.objects.get(slug='claand')
        self.assertIs(empresa)
        numeros_list = empresa.numerotelefonico_set.all()
        self.assertTrue('numeros_list' in response.context)
        redes_list = empresa.redsocial_set.all()
        self.assertTrue('redes_list' in response.context)
        contactos_list = Contacto.objects.filter(empresa=empresa)
        self.assertTrue('contactos_list' in response.context)
        
    def test_vista_empresas(self):
        """ Probar si se muestran todas las empresas
        """
        login = self.client.login(username='temporary', password='temporary')
        self.assertTrue(login)
        response = self.client.get(reverse('empresas:consultar_empresas'))
        self.assertEqual(response.status_code, 200)
        empresas = Empresa.objects.all()
        self.assertTrue('empresas_list' in response.context)
        self.assertCountEqual(response.context['empresas_list'], empresas)


        