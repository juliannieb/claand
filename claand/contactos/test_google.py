
import base64
import imp
import os
import pickle
import sys
import unittest

from oauth2client.client import Credentials
from oauth2client.client import Flow

# Mock a Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_settings'
sys.modules['django_settings'] = imp.new_module('django_settings')

from oauth2client.django_orm import CredentialsField
from oauth2client.django_orm import FlowField


class TestCredentialsField(unittest.TestCase):
  def setUp(self):
    self.field = CredentialsField()
    self.credentials = Credentials()
    self.pickle = base64.b64encode(pickle.dumps(self.credentials))

  def test_field_is_text(self):
    self.assertEquals(self.field.get_internal_type(), 'TextField')

  def test_field_unpickled(self):
    self.assertTrue(isinstance(self.field.to_python(self.pickle), Credentials))

  def test_field_pickled(self):
    prep_value = self.field.get_db_prep_value(self.credentials,
                                              connection=None)
    self.assertEqual(prep_value, self.pickle)


class TestFlowField(unittest.TestCase):
  def setUp(self):
    self.field = FlowField()
    self.flow = Flow()
    self.pickle = base64.b64encode(pickle.dumps(self.flow))

  def test_field_is_text(self):
    self.assertEquals(self.field.get_internal_type(), 'TextField')

  def test_field_unpickled(self):
    self.assertTrue(isinstance(self.field.to_python(self.pickle), Flow))

  def test_field_pickled(self):
    prep_value = self.field.get_db_prep_value(self.flow, connection=None)
    self.assertEqual(prep_value, self.pickle)