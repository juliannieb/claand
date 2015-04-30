from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase
from django.contrib.auth.models import User, Group

class PrincipalFunctionalTests(LiveServerTestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def tearDown(self):
        self.browser.quit()

    def test_admin_site(self):
        """ test para probar interacción básica de login al admin:
        - ir a la vista de admin
        - ingresar usuario y contraseña
        - redirección a página de Administración del sitio
        """
        # user opens web browser, navigates to admin page
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Claand', body.text)
        # users types in username and passwords and presses enter
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        # login credentials are correct, and the user is redirected to the main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Administración del sitio', body.text)


    def test_login_vendedor(self):
        """ test para probar interacción básica de login:
        - ir a la vista de login
        - ingresar usuario y contraseña
        - redirección a página de inicio(index)
        """
        # vendedor abre 
        self.browser.get(self.live_server_url + '/principal/login/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Ingresa con tu usuario', body.text)
        # users types in username and passwords and presses enter
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('Julian')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('julian')
        password_field.send_keys(Keys.RETURN)
        # login credentials are correct, and the user is redirected to the main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Inicio', body.text)
        self.assertIn('Registrar contacto', body.text)
        self.assertIn('Registrar llamada', body.text)
        self.assertIn('Registrar cotización', body.text)
        self.assertIn('Consultar', body.text)

    def test_login_director(self):
        """ test para probar interacción básica de login de un director:
        - ir a la vista de login
        - ingresar usuario y contraseña
        - redirección a página de inicio(index)
        """
        # vendedor abre 
        self.browser.get(self.live_server_url + '/principal/login/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Ingresa con tu usuario', body.text)
        # users types in username and passwords and presses enter
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        # login credentials are correct, and the user is redirected to the main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Inicio', body.text)
        self.assertIn('Recordatorios', body.text)
        self.assertIn('Notas', body.text)
        self.assertIn('Consultar', body.text)
        # consultar un vendedor:
        self.browser.find_element_by_link_text('Consultar').click()
        self.browser.find_element_by_link_text('Vendedores').click()
        # revisar que esten todos los vendedores

    def test_registrar_vendedor(self):
        """ Test para registrar un vendedor
        """
        self.browser.get(self.live_server_url + '/principal/login/')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

        self.browser.find_element_by_link_text('Consultar').click()
        self.browser.find_element_by_link_text('Vendedores').click()
        self.browser.find_element_by_id('registrar_vendedor').click()

        nombre_field = self.browser.find_element_by_id('id_nombre')
        nombre_field.send_keys('tulio')
        apellido_field = self.browser.find_element_by_id('id_apellido')
        apellido_field.send_keys('elegante')
        correo_field = self.browser.find_element_by_id('id_correo_electronico')
        correo_field.send_keys('tulio@abc.com')
        username_field = self.browser.find_element_by_id('id_usuario')
        username_field.send_keys('tulio')
        password_field = self.browser.find_element_by_id('id_password')
        password_field.send_keys('tulio')
        self.browser.find_element_by_id('registrar_vendedor').click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Operación exitosa', body.text)

        self.browser.find_element_by_link_text('Consultar').click()
        self.browser.find_element_by_link_text('Vendedores').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('tulio elegante', body.text)








