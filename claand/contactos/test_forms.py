from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor
from contactos.models import Contacto
from empresas.models import Empresa

from contactos.forms import LlamadaForm, NotaForm, ContactoForm


class FormasContactos(TestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    def setUp(self):
        pass


    def tearDown(self):
        pass   


    def test_registrar_llamada_valida(self):
        """ probar registrar una llamada con valores válidos
        """
        contacto = Contacto.objects.get(id=1)
        descripcion = "prueba"
        data = {'contacto' : contacto.id, 'descripcion' : descripcion}
        form_llamada = LlamadaForm(data=data)
        self.assertTrue(form_llamada.is_valid())

    def test_registrar_llamada_invalida(self):
        """ probar registrar una llamada inválida: 
        - sin descripcion
        - contacto inexistente
        """
        contacto = Contacto.objects.get(id=1)
        descripcion = ""
        data = {'contacto' : contacto.id, 'descripcion' : descripcion}
        form_llamada = LlamadaForm(data=data)
        self.assertFalse(form_llamada.is_valid())
        descripcion = "prueba"
        data = {'descripcion' : descripcion}
        self.assertFalse(form_llamada.is_valid())

    def test_registrar_nota_valida(self):
        """ probar registrar una nota con valores válidos
        """
        contacto = Contacto.objects.get(id=1)
        descripcion = "prueba"
        clasificacion = 2
        data = {'contacto' : contacto.id, 'descripcion' : descripcion,
                'clasificacion' : clasificacion}
        form_nota = NotaForm(data=data)
        self.assertTrue(form_nota.is_valid())

    def test_registrar_nota_invalida(self):
        """ probar registrar una nota con valores inválidos:
        - clasificacion inexistente
        - descripcion vacía
        - contacto inexistente
        """
        contacto = Contacto.objects.get(id=1)
        descripcion = "prueba"
        clasificacion = 5

        data = {'contacto' : contacto.id, 'descripcion' : descripcion,
                'clasificacion' : clasificacion}
        form_nota = NotaForm(data=data)
        self.assertFalse(form_nota.is_valid())

        data = {'contacto' : -1, 'descripcion' : descripcion,
                'clasificacion' : clasificacion}
        form_nota = NotaForm(data=data)
        self.assertFalse(form_nota.is_valid())

        data = {'contacto' : contacto.id, 'descripcion' : "",
                'clasificacion' : clasificacion}
        form_nota = NotaForm(data=data)
        self.assertFalse(form_nota.is_valid())

    def test_registrar_contacto_invalido(self):
        """ Probar registrar un contacto con valores inválidos:
        - Sin empresa ni área
        TODO: probar con area y no otras.
        """
        nombre = "Marquicio"
        apellido = "Lopez"
        correo_electronico = "marquicio@abc.com"
        calificacion = 1
        is_cliente = True
        data = {'nombre' : nombre, 'apellido' : apellido,
                'correo_electronico' : correo_electronico, 
                'calificacion' : calificacion, 'is_cliente' : is_cliente}
        form_contacto = ContactoForm(data=data)
        self.assertFalse(form_contacto.is_valid())

    def test_registrar_contacto_valido(self):
        """ Probar registrar un contacto con valores válidos
        TO-DO: Cargar todos los datos necesarios (pertenece, etc)
        """
        pass


