# from django.urls import resolve
# from django.core.urlresolvers import resolve
from django.test import TestCase
# from django.http import HttpRequest
# from django.template.loader import render_to_string

# from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    # Commented out test below; already tested implicitly with Django Test Client
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))
