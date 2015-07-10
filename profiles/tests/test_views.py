from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from ..views import create_profile

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class CreateProfileTestView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create(
            username='user1', password='1', first_name='John', last_name='Doe', email="jd@jd.com"
        )

    def test_displays_correct_form(self):
        request = self.factory.get(reverse('create_profile'))
        request.user = self.user
        response = create_profile(request)
        view_html = response.content.decode()
        self.assertIn('<form', view_html)
        self.assertIn('profile_picture', view_html)
        self.assertIn('gender', view_html)
        self.assertIn('birthday', view_html)
