from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from ..models import Notification
from ..views import view_notifications
from profiles.models import UserProfile

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class ViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create(
            username='user1', password='1', first_name='John', last_name='Doe', email="jd@jd.com"
        )


class ViewNotificationsViewTest(ViewTestCase):

    def test_displays_correct_user_infromation(self):
        request = self.factory.get(reverse('view_notifications'))
        request.user = self.user
        UserProfile.objects.create(user=self.user, gender='M', birthday='1990-05-12')
        response = view_notifications(request)
        view_html = response.content.decode()
        self.assertIn("You don't have any notifications at this moment!", view_html)
        Notification.objects.create(user=self.user, notification_type='Friend Request',
                                    content='No One wants to be your friend.')
        response = view_notifications(request)
        view_html = response.content.decode()
        self.assertIn("No One wants to be your friend.", view_html)
