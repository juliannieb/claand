from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

from principal.models import Vendedor


class Contacto(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def tearDown(self):
        pass
        
    def test_contacto_usuario_registrado(self):
        """ test para checar si un usuario registrado puede entrar a la vista
        de consultar contactos sin redirecciones 
        """
        login = self.client.login(username='temporary', password='temporary')
        self.assertTrue(login)
        response = self.client.get(reverse('contactos:consultar_contactos'))
        self.assertEqual(response.status_code, 200)

    def test_contacto_usuario_no_registrado(self):
        """ test para checar si un usuario no registrado es redirigido al login
        al intentar entrar a consultar contactos.
        """
        response = self.client.get(reverse('contactos:consultar_contactos'))
        self.assertEqual(response.status_code, 302)
