from datetime import datetime

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from principal.models import Vendedor

class ModelosPrincipal(TestCase):
	fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']

	def setUp(self):
		self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

	def tearDown(self):
		pass

	def test_save_vendedor(self):
		""" test para probar la creación de un vendedor
		"""
		vendedor_prueba = Vendedor.objects.create(user=self.usuario)
		self.assertIsNotNone(vendedor_prueba.user.groups.get(name='vendedor'))
