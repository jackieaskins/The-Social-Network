from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import StatusPost, StatusComment
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

    def generate_status_post(self, user_profile):
        status_post = StatusPost()
        status_post.user_profile = user_profile
        status_post.text = 'Lorem ipsum, blah, blah, blah'
        status_post.save()
        return status_post


class StatusPostTest(ModelTestCase):

    def test_saving_and_retrieving_status_posts(self):
        user1 = self.generate_user('woo')
        user2 = self.generate_user('yoo')
        profile1 = self.generate_user_profile(user1)
        profile2 = self.generate_user_profile(user2)

        first_post = StatusPost()
        first_post.text = 'The Social Network is soooooooo cool! Wooo!'
        first_post.user_profile = profile1
        first_post.save()

        second_post = StatusPost()
        second_post.text = 'I am so amazed at how much I love this site!'
        second_post.user_profile = profile2
        second_post.save()

        saved_posts = StatusPost.objects.all()
        self.assertEqual(saved_posts.count(), 2)

        first_saved_post = saved_posts[0]
        second_saved_post = saved_posts[1]
        self.assertEqual(first_saved_post.text, 'The Social Network is soooooooo cool! Wooo!')
        self.assertEqual(second_saved_post.text, 'I am so amazed at how much I love this site!')
        self.assertEqual(first_saved_post.user_profile.user, user1)
        self.assertEqual(second_saved_post.user_profile.user, user2)
        self.assertEqual(first_saved_post.likes, 0)

    def test_cannot_save_empty_status_posts(self):
        post = StatusPost(text='')
        with self.assertRaises(ValidationError):
            bob = self.generate_user('bob')
            post.user_profile = self.generate_user_profile(bob)
            post.save()
            post.full_clean()


class StatusCommentTest(ModelTestCase):

    def test_saving_and_retrieving_status_comments(self):
        user1 = self.generate_user('woo')
        user2 = self.generate_user('yoo')
        profile1 = self.generate_user_profile(user1)
        profile2 = self.generate_user_profile(user2)
        status_post = self.generate_status_post(profile1)

        first_comment = StatusComment()
        first_comment.status_post = status_post
        first_comment.user_profile = profile2
        first_comment.text = 'Lorem impsum, blah, blah'
        first_comment.save()

        second_comment = StatusComment()
        second_comment.status_post = status_post
        second_comment.user_profile = profile1
        second_comment.text = 'Lorem impsum, blah'
        second_comment.save()

        saved_comments = StatusComment.objects.all()
        self.assertEqual(saved_comments.count(), 2)

        first_saved_comment = saved_comments[0]
        second_saved_comment = saved_comments[1]
        self.assertEqual(first_saved_comment.text, 'Lorem impsum, blah, blah')
        self.assertEqual(second_saved_comment.text, 'Lorem impsum, blah')
        self.assertEqual(first_saved_comment.status_post, status_post)
        self.assertEqual(second_saved_comment.status_post, status_post)
        self.assertEqual(first_saved_comment.user_profile.user, user2)
        self.assertEqual(second_saved_comment.user_profile.user, user1)
        self.assertEqual(first_saved_comment.likes, 0)

    def test_cannot_save_empty_status_comments(self):
        comment = StatusComment(text='')
        with self.assertRaises(ValidationError):
            bob = self.generate_user('bob')
            bob_profile = self.generate_user_profile(bob)
            comment.user_profile = bob_profile
            comment.status_post = self.generate_status_post(bob_profile)
            comment.save()
            comment.full_clean()
