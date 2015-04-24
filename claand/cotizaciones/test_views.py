from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor


class VistasCotizaciones(TestCase):
    def setUp(self):
        grupo_vendedor = Group.objects.get_or_create(name="vendedor")[0]
        self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.vendedor = User.objects.create_user('julian', 'julian@abc.com', 'julian')
        self.vendedor.groups.add(grupo_vendedor)

    def tearDown(self):
        pass

    def test_cotizaciones_usuario_no_autenticado(self):
        """ test para checar si un usuario no registrado es redirigido al login
        al intentar entrar a las vistas del app de cotizacion.
        """
        response = self.client.get(reverse('cotizaciones:consultar_cotizaciones'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('cotizaciones:consultar_ventas'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('cotizaciones:registrar_cotizacion'))
        self.assertEqual(response.status_code, 302)
        