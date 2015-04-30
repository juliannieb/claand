from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase
from django.contrib.auth.models import User, Group

class PrincipalFunctionalTests(LiveServerTestCase):
    fixtures = ['contactos.json', 'empresas.json', 'cotizaciones.json', 'principal.json', 'users.json']
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.usuario = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        grupo_vendedor = Group.objects.get_or_create(name="vendedor")[0]
        tulio = User.objects.get(username='Tulio')
        tulio.groups.add(grupo_vendedor)

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
        username_field.send_keys('Tulio')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('tulio')
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

