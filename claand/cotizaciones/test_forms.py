from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor
from contactos.models import Contacto
from empresas.models import Empresa

from cotizaciones.forms import CotizacionForm, VentaForm, PagoForm


class FormasCotizaciones(TestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    def setUp(self):
        pass

    def tearDown(self):
        pass   

    def test_registrar_cotizacion_valida(self):
        """ probar registrar una cotización con datos válidos
        """
        contacto = Contacto.objects.get(id=1)
        monto = 123900123.66
        descripcion = "troqueladoras para mr. marquicio"
        data = {'contacto' : contacto.id, 'monto' : monto, 'descripcion' : descripcion}
        form_cotizacion = CotizacionForm(data=data)
        self.assertTrue(form_cotizacion.is_valid())

    def test_registrar_cotizacion_invalida(self):
        """ probar registrar una cotización con datos inválidos:
        - monto negativo
        - sin descripcion
        - sin contacto
        """
        contacto = Contacto.objects.get(id=1)
        monto = -123900123.66
        descripcion = "troqueladoras para mr. marquicio"
        data = {'contacto' : contacto.id, 'monto' : monto, 'descripcion' : descripcion}
        form_cotizacion = CotizacionForm(data=data)
        self.assertFalse(form_cotizacion.is_valid())

        data = {'contacto' : contacto.id, 'monto' : monto, 'descripcion' : ""}
        form_cotizacion = CotizacionForm(data=data)
        self.assertFalse(form_cotizacion.is_valid())

        data = {'contacto' : 123123, 'monto' : monto, 'descripcion' : descripcion}
        form_cotizacion = CotizacionForm(data=data)
        self.assertFalse(form_cotizacion.is_valid())

    def test_registrar_venta_valida(self):
        """ Prueba de registrar una venta con datos válidos
        """
        monto_total = 123987129387.1
        data = {'monto_total' : monto_total}
        form_venta = VentaForm(data=data)
        self.assertTrue(form_venta.is_valid())

    def test_registrar_venta_invalida(self):
        """ Prueba de registrar una venta con datos inválidos:
        - monto inexistente
        - monto negativo
        """
        monto_total = -123123123
        data = {'monto_total' : monto_total}
        form_venta = VentaForm(data=data)
        self.assertFalse(form_venta.is_valid())

        data = {}
        form_venta = VentaForm(data=data)
        self.assertFalse(form_venta.is_valid())

    def test_registrar_pago_valido(self):
        """ Prueba de registrar un pago con monto válido.
        """
        monto = 879879858697
        data = {'monto' : monto}
        form_pago = PagoForm(data=data)
        self.assertTrue(form_pago.is_valid())

    def test_registrar_pago_invalido(self):
        """ Prueba de registrar un pago con datos inválidos:
        - Monto negativo
        - Monto inexistente
        """
        monto = -1212
        data = {'monto' : monto}
        form_pago = PagoForm(data=data)
        self.assertFalse(form_pago.is_valid())

        data = {}
        form_pago = PagoForm(data=data)
        self.assertFalse(form_pago.is_valid())



