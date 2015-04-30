from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase
from django.contrib.auth.models import User, Group

class ContactosAdminTests(LiveServerTestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        grupo_vendedor = Group.objects.get_or_create(name="vendedor")[0]
        self.browser.get(self.live_server_url + '/principal/login/')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

    def tearDown(self):
        self.browser.quit()

    def test_crear_editar_borrar_nota(self):
        """ test de creación, edición y eliminación de una nota
        """
        self.browser.find_element_by_link_text('Notas').click()
        self.browser.find_element_by_id('crear_nota').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Registrar nota', body.text)
        el = self.browser.find_element_by_id('id_contacto')
        # elegir contacto Marquicio
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'Marquicio López':
                option.click()
                break
        descripcion = self.browser.find_element_by_id('id_descripcion')
        # poner descripcion
        descripcion.send_keys('Saca el copy paste')
        # click registrar
        registrar = self.browser.find_element_by_id('registrar_nota')
        registrar.click()
        body = self.browser.find_element_by_tag_name('body')
        # operación exitosa?
        self.assertIn('Operación exitosa', body.text)
        # volver a notas
        self.browser.find_element_by_link_text('Notas').click()
        




