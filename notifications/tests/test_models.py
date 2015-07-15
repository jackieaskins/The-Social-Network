from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Notification
from profiles.models import UserProfile

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

PROF_PIC_ROOT = settings.MEDIA_ROOT + '/profile_pictures'


class ModelTestCase(TestCase):
    def generate_user(self, user_name):
        User = get_user_model()
        return User.objects.create(
            username=user_name, password='1', first_name='John', last_name='Doe', email="jd@jd.com"
        )

    def generate_user_profile(self, user):
        user_profile = UserProfile()
        user_profile.user = user
        user_profile.gender = 'M'
        user_profile.birthday = '1985-05-21'
        user_profile.save()
        return user_profile


class NotificationTest(ModelTestCase):

    def test_saving_and_retrieving_notifications(self):
        user1 = self.generate_user('user1')
        user2 = self.generate_user('user2')

        notification1 = Notification()
        notification1.user = user1
        notification1.notification_type = 'friend request'
        notification1.content = 'Bob Marley wants to be your friend.'
        notification1.status = 1
        notification1.save()

        notification2 = Notification()
        notification2.user = user2
        notification2.notification_type = 'friend request'
        notification2.content = 'Jose Illiad wants to be your friend.'
        notification2.save()

        saved_notifications = Notification.objects.all()
        self.assertEquals(2, saved_notifications.count())

        first_saved_notification = saved_notifications[0]
        second_saved_notification = saved_notifications[1]
        self.assertEqual(first_saved_notification.user, user1)
        self.assertEqual(second_saved_notification.user, user2)
        self.assertEqual(first_saved_notification.notification_type, 'friend request')
        self.assertEqual(second_saved_notification.notification_type, 'friend request')
        self.assertIn('Bob Marley', first_saved_notification.content)
        self.assertIn('Jose Illiad', second_saved_notification.content)
        self.assertEqual(first_saved_notification.status, 1)
        self.assertEqual(second_saved_notification.status, 0)
