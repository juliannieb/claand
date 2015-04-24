from datetime import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor
from contactos.models import Contacto, Llamada, Nota


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

    def test_str_contacto(self):
        """ Test para probar el método str() del modelo de contacto
        """
        contacto_prueba = Contacto.objects.create(nombre="Julián", apellido="Niebieskikwiat")
        self.assertEqual("Julián Niebieskikwiat", str(contacto_prueba))

    def test_str_nota(self):
        """ Test para probar el método str() del modelo de nota 
        """
        contacto_prueba = Contacto.objects.get(id=1)
        descripcion = "Marquicio y tulio el elegante."
        nota_prueba = Nota.objects.create(contacto=contacto_prueba, descripcion=descripcion)
        self.assertEqual(descripcion, str(nota_prueba))

    def test_str_llamada(self):
        """ Test para probar el str() de llamada 
        """
        descripcion = "asdfblasd;fkjnsa;kfj sdaf;jknasd;kfjasd;fjk asdf;kjasdfjas;dfjkn asdf;nasdf"
        fecha = datetime.now()
        contacto_prueba = Contacto.objects.get(id=1)
        llamada_prueba = Llamada.objects.create(contacto=contacto_prueba, descripcion=descripcion, fecha=fecha)
        self.assertEqual(descripcion[:30], str(llamada_prueba))







