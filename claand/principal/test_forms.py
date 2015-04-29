from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from contactos.models import Contacto

from cotizaciones.forms import CotizacionForm, VentaForm, PagoForm


class FormasPrincipal(TestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    def setUp(self):
        grupo_vendedor = Group.objects.get_or_create(name="vendedor")[0]
        self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.vendedor = User.objects.create_user('julian', 'julian@abc.com', 'julian')
        self.vendedor.groups.add(grupo_vendedor)

    def tearDown(self):
        pass   

    def test_login_invalido(self):
        """ probar autenticación inválida:
        - usuario invalido y password valido
        - usuario valido y password invalido 
        - usuario invalido y password invalido
        """
        login = self.client.login(username='asasas', password='temporary')
        self.assertFalse(login)
        login = self.client.login(username='temporary', password='asdasda')
        self.assertFalse(login)
        login = self.client.login(username='julio', password='julio')
        self.assertFalse(login)

    def test_login_valido(self):
        """ Probar autenticación válida
        """
        login = self.client.login(username='temporary', password='temporary')
        self.assertTrue(login)