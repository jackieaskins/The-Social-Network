from django.template.loader import render_to_string
from django.test import TestCase

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class HomeViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        expected_html = render_to_string('network/index.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_extends_base_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')
