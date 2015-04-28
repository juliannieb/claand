from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor
from contactos.models import Contacto
from empresas.models import Empresa, Estado, Municipio

from empresas.forms import EmpresaForm, DireccionForm, NumeroTelefonicoForm, RedSocialForm

class FormasEmpresas(TestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    def setUp(self):
        pass


    def tearDown(self):
        pass 


    def test_registrar_empresa_valida(self):
        """ registrar una empresa con datos válidos
        """
        nombre = "clAAAAnd"
        rfc = "AJAIIO98HBASK"
        data = {'nombre' : nombre, 'rfc' : rfc}
        form_empresa = EmpresaForm(data=data)
        self.assertTrue(form_empresa.is_valid())


    def test_registrar_empresa_invalida(self):
        """ registrar una empresa con datos inválidos:
        - rfc de menos de 13 letras
        - rfc de mas de 13 letras
        - nombre inexistente
        - rfc inexistente
        """
        nombre = "clAAAAnd"
        rfc = "aaaAA"
        data = {'nombre' : nombre, 'rfc' : rfc}
        form_empresa = EmpresaForm(data=data)
        self.assertFalse(form_empresa.is_valid())

        rfc = "AAaAaaaAZZZZZZZAAAAAaaaa"
        data = {'nombre' : nombre, 'rfc' : rfc}
        form_empresa = EmpresaForm(data=data)
        self.assertFalse(form_empresa.is_valid())

        rfc = "AJAIIO98HBASK"
        data = {'nombre' : "", 'rfc' : rfc}
        form_empresa = EmpresaForm(data=data)
        self.assertFalse(form_empresa.is_valid())

        data = {'nombre' : "claand", 'rfc' : ""}
        form_empresa = EmpresaForm(data=data)
        self.assertFalse(form_empresa.is_valid())

    def test_registrar_direccion_valida(self):
        """ registrar una dirección con datos válidos
        """
        estado = Estado.objects.get(nombre="Oaxaca")
        direccion = "calle 5000 a lado del piso derretido"
        municipio = Municipio.objects.get(nombre="Abejones")
        data = {'estado':estado.id, 'direccion':direccion, 'municipio':municipio.id}
        form_direccion = DireccionForm(data=data)
        self.assertTrue(form_direccion.is_valid())


    def test_registrar_direccion_invalida(self):
        """ registrar una dirección con datos inválidos:
        - estado inexistente
        - direccion inexistente
        - municipio inexistente
        """
        direccion = "calle 5000 a lado del piso derretido"
        data = {'estado':-1, 'direccion':direccion, 'municipio':1}
        form_direccion = DireccionForm(data=data)
        self.assertFalse(form_direccion.is_valid())

        direccion = ""
        data = {'estado':1, 'direccion':direccion, 'municipio':1}
        form_direccion = DireccionForm(data=data)
        self.assertFalse(form_direccion.is_valid())

        direccion = "calle 5000 a lado del piso derretido"
        data = {'estado':1, 'direccion':direccion, 'municipio':-1}
        form_direccion = DireccionForm(data=data)
        self.assertFalse(form_direccion.is_valid())

    def test_registrar_numero_valido(self):
        """ registrar un numero telefónico válido
        """
        numero = 4414579611
        data = {'numero' : numero, 'tipo_numero': 1}
        form_numero = NumeroTelefonicoForm(data=data)
        self.assertTrue(form_numero.is_valid())

    def test_registrar_numero_invalido(self):
        """ registrar un numero telefónico inválido:
        - numero inexistente
        - tipo de numero inexistente
        """
        numero = 4414579611
        data = {'tipo_numero': 1}
        form_numero = NumeroTelefonicoForm(data=data)
        self.assertFalse(form_numero.is_valid())

        numero = 4414579611
        data = {'numero' : numero, 'tipo_numero': -1}
        form_numero = NumeroTelefonicoForm(data=data)
        self.assertFalse(form_numero.is_valid())

    def test_registrar_red_social_valida(self):
        """ registrar una red social válida
        """
        link = "https://www.facebook.com/julian.ng.9?fref=ts"
        data = {'link' : link, 'tipo_red_social' : 1}
        form_red = RedSocialForm(data=data)
        self.assertTrue(form_red.is_valid())

    def test_registrar_red_social_invalida(self):
        """ registrar una red social con datos inválidos:
        - link inexistente
        - link invalido 
        - tipo red social inexistente
        """
        link = ""
        data = {'link' : link, 'tipo_red_social' : 1}
        form_red = RedSocialForm(data=data)
        self.assertFalse(form_red.is_valid())

        link = "aaaaaaaa"
        data = {'link' : link, 'tipo_red_social' : 1}
        form_red = RedSocialForm(data=data)
        self.assertFalse(form_red.is_valid())

        link = "https://www.facebook.com/julian.ng.9?fref=ts"
        data = {'link' : link, 'tipo_red_social' : -1}
        form_red = RedSocialForm(data=data)
        self.assertFalse(form_red.is_valid())




