from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor


class VistasEmpresas(TestCase):
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


        