from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from network.models import StatusPost, UserProfile

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

PROF_PIC_ROOT = settings.MEDIA_ROOT + '/profile_pictures'


class ModelTestCase(TestCase):
    def generate_user(self, user_name):
        User = get_user_model()
        return User.objects.create(
            username=user_name, password='1', first_name='John', last_name='Doe', email="jd@jd.com"
        )


class StatusPostTest(ModelTestCase):

    def test_saving_and_retrieving_status_posts(self):
        user1 = self.generate_user('woo')
        user2 = self.generate_user('yoo')

        first_post = StatusPost()
        first_post.text = 'The Social Network is soooooooo cool! Wooo!'
        first_post.user = user1
        first_post.save()

        second_post = StatusPost()
        second_post.text = 'I am so amazed at how much I love this site!'
        second_post.user = user2
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
            post.user = self.generate_user('bob')
            post.save()
            post.full_clean()


class UserProfileTest(ModelTestCase):

    def test_profile_pictures_default_correctly(self):

        user1 = self.generate_user('user1')
        user2 = self.generate_user('user2')
        user3 = self.generate_user('user3')

        first_profile = UserProfile()
        first_profile.user = user1
        first_profile.gender = 'M'
        first_profile.birthday = '1995-04-28'
        first_profile.save()

        second_profile = UserProfile()
        second_profile.user = user2
        second_profile.gender = 'F'
        second_profile.birthday = '1996-07-15'
        second_profile.save()

        third_profile = UserProfile()
        third_profile.user = user3
        third_profile.gender = 'F'
        third_profile.birthday = '1996-04-24'
        third_profile.profile_picture = PROF_PIC_ROOT + '/dog.jpg'
        third_profile.save()

        self.assertEqual(first_profile.profile_picture, PROF_PIC_ROOT + '/default_male.png')
        self.assertEqual(second_profile.profile_picture, PROF_PIC_ROOT + '/default_female.png')
        self.assertEqual(third_profile.profile_picture, PROF_PIC_ROOT + '/dog.jpg')
