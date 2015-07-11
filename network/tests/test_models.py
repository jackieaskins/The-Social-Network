from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import StatusPost
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


class StatusPostTest(ModelTestCase):

    def test_saving_and_retrieving_status_posts(self):
        user1 = self.generate_user('woo')
        user2 = self.generate_user('yoo')
        profile1 = self.generate_user_profile(user1)
        profile2 = self.generate_user_profile(user2)

        first_post = StatusPost()
        first_post.text = 'The Social Network is soooooooo cool! Wooo!'
        first_post.user = user1
        first_post.user_profile = profile1
        first_post.save()

        second_post = StatusPost()
        second_post.text = 'I am so amazed at how much I love this site!'
        second_post.user = user2
        second_post.user_profile = profile2
        second_post.save()

        saved_posts = StatusPost.objects.all()
        self.assertEqual(saved_posts.count(), 2)

        first_saved_post = saved_posts[0]
        second_saved_post = saved_posts[1]
        self.assertEqual(first_saved_post.text, 'The Social Network is soooooooo cool! Wooo!')
        self.assertEqual(second_saved_post.text, 'I am so amazed at how much I love this site!')
        self.assertEqual(first_saved_post.user, user1)
        self.assertEqual(second_saved_post.user, user2)
        self.assertEqual(first_saved_post.likes, 0)

    def test_cannot_save_empty_status_posts(self):
        post = StatusPost(text='')
        with self.assertRaises(ValidationError):
            bob = self.generate_user('bob')
            post.user = bob
            post.user_profile = self.generate_user_profile(bob)
            post.save()
            post.full_clean()
