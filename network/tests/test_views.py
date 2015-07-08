from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from network.views import home


class HomeViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('network/index.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_extends_base_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')
