from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Notification
from profiles.models import UserProfile

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class ModelTestCase(TestCase):
    def generate_user(self, user_name):
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
        notification1.to_user = user1
        notification1.type_id = 0
        notification1.content = 'Bob Marley wants to be your friend.'
        notification1.status = 1
        notification1.save()

        notification2 = Notification()
        notification2.to_user = user2
        notification2.type_id = 0
        notification2.content = 'Jose Illiad wants to be your friend.'
        notification2.save()

        saved_notifications = Notification.objects.all()
        self.assertEquals(2, saved_notifications.count())

        first_saved_notification = saved_notifications[0]
        second_saved_notification = saved_notifications[1]
        self.assertEqual(first_saved_notification.to_user, user1)
        self.assertEqual(second_saved_notification.to_user, user2)
        self.assertEqual(first_saved_notification.type_id, 0)
        self.assertEqual(second_saved_notification.type_id, 0)
        self.assertIn('Bob Marley', first_saved_notification.content)
        self.assertIn('Jose Illiad', second_saved_notification.content)
        self.assertEqual(first_saved_notification.status, 1)
        self.assertEqual(second_saved_notification.status, 0)
