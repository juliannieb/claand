from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor
from contactos.models import Contacto


class ModelosContacto(TestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    def setUp(self):
        pass


    def tearDown(self):
        pass   

    def test_slug_unico_contacto(self):
        """ Test para probar si el slug de dos contactos es diferente en el caso en que
        haya dos con el mismo nombre 
        """
        contacto_a = Contacto.objects.create(nombre="Juan", apellido="Perez", \
            correo_electronico="j@b.com")
        contacto_b = Contacto.objects.create(nombre="Juan", apellido="Perez", \
            correo_electronico="a@b.com")
        self.assertNotEqual(contacto_a.slug, contacto_b.slug)
        contacto_c = Contacto.objects.create(nombre="Juan", apellido="Perez", \
            correo_electronico="c@b.com")
        self.assertNotEqual(contacto_a.slug, contacto_c.slug)
        self.assertNotEqual(contacto_b.slug, contacto_c.slug)




