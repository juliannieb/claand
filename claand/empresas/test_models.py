from datetime import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from empresas.models import Empresa, Estado, Municipio

class ModelosEmpresas(TestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    def setUp(self):
        pass

    def tearDown(self):
        pass  

    def test_slug_unico_contacto(self):
        """ Test para probar si el slug de dos empresas es diferente en el caso en que
        haya mas de una con el mismo nombre.
        """
        empresa_a = Empresa.objects.create(nombre="Claand", rfc="CLAJSHAUEIOPS")
        empresa_b = Empresa.objects.create(nombre="cLaaNd", rfc="CLAJSHAOEIOPS")
        self.assertNotEqual(empresa_a.slug, empresa_b.slug)
        empresa_c = Empresa.objects.create(nombre="clAAnD", rfc="CIAJSHAOEIOPS")
        self.assertNotEqual(empresa_a.slug, empresa_c.slug)
        self.assertNotEqual(empresa_b.slug, empresa_c.slug)


    def test_str_empresa(self):
        """ Test para probar el str() del modelo de Empresa
        """
        nombre = "cllAAAnD"
        empresa_b = Empresa.objects.create(nombre=nombre, rfc="CLAJSHAOEIOPS")
        self.assertEqual(nombre, str(empresa_b))

    def test_str_estado(self):
        """ test para el str() del modelo estado 
        """
        oaxaca = Estado.objects.get(nombre="Oaxaca")
        self.assertIsNotNone(oaxaca)
        self.assertEqual(oaxaca.nombre, str(oaxaca))

    def test_str_municipio(self):
        """ Test para probar el str() de Municipio
        """
        nombre = "Hostotipaquillo"
        municipio = Municipio.objects.get(nombre=nombre)
        self.assertIsNotNone(municipio)
        self.assertEqual(nombre, str(municipio))
