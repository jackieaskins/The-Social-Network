from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from ..views import create_profile, view_profile
from ..models import UserProfile

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class ViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            username='user1', password='1', first_name='John', last_name='Doe', email="jd@jd.com"
        )


class CreateProfileViewTest(ViewTestCase):

    def test_displays_correct_form(self):
        request = self.factory.get(reverse('create_profile'))
        request.user = self.user
        response = create_profile(request)
        view_html = response.content.decode()
        self.assertIn('<form', view_html)
        self.assertIn('profile_picture', view_html)
        self.assertIn('gender', view_html)
        self.assertIn('birthday', view_html)


class ViewProfileViewTest(ViewTestCase):

    def test_displays_correct_user_infromation(self):
        request = self.factory.get(reverse('view_profile', args=[self.user.username]))
        request.user = self.user
        UserProfile.objects.create(user=self.user, gender='M', birthday='1990-05-12')
        response = view_profile(request, request.user.username)
        view_html = response.content.decode()
        self.assertIn('Your Profile', view_html)
        self.assertIn('Full Name: John Doe', view_html)
        self.assertIn('Gender: Male', view_html)
        self.assertIn('Birthday: May 12, 1990', view_html)
