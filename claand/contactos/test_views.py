from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor


class VistasContacto(TestCase):
    def setUp(self):
        grupo_vendedor = Group.objects.get_or_create(name="vendedor")[0]
        self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.vendedor = User.objects.create_user('julian', 'julian@abc.com', 'julian')
        self.vendedor.groups.add(grupo_vendedor)

    def tearDown(self):
        pass
        
    def test_contacto_usuario_registrado(self):
        """ test para checar si un usuario registrado puede entrar a la vista
        de consultar contactos sin redirecciones, si cuenta con la lista de contactos
        y si no es vendedor.
        """
        login = self.client.login(username='temporary', password='temporary')
        self.assertTrue(login)
        response = self.client.get(reverse('contactos:consultar_contactos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('contactos_list' in response.context)
        self.assertTrue('no_es_vendedor' in response.context)
        self.assertTrue(response.context['no_es_vendedor'])

    def test_contacto_usuario_no_registrado(self):
        """ test para checar si un usuario no registrado es redirigido al login
        al intentar entrar a consultar contactos.
        """
        response = self.client.get(reverse('contactos:consultar_contactos'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:registrar_contactos'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:registrar_contacto'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:registrar_llamada'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:consultar_notas'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:registrar_nota'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:consultar_recordatorios'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:registrar_recordatorio'))
        self.assertEqual(response.status_code, 302)

    def test_acceso_vendedor(self):
        """ test para validar que se redireccione a un vendedor si intenta
        entrar a secciones del director 
        """
        login = self.client.login(username='julian', password='julian')
        self.assertTrue(login)
        response = self.client.get(reverse('contactos:consultar_notas'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:registrar_nota'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:consultar_recordatorios'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('contactos:registrar_recordatorio'))
        self.assertEqual(response.status_code, 302)


