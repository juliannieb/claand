from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor


class ModelosContacto(TestCase):
    def setUp(self):
    	pass
        # grupo_vendedor = Group.objects.get_or_create(name="vendedor")[0]
        # self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        # self.vendedor = User.objects.create_user('julian', 'julian@abc.com', 'julian')
        # self.vendedor.groups.add(grupo_vendedor)

    def tearDown(self):
        pass   


    def test_slug_unico_contacto(self):
    	""" Test para probar si la función de save maneja correctamente el caso en que
    	haya dos contactos con el mismo nombre 
    	"""
    	pass


