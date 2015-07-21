from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import StatusPost, StatusComment, PostLike, CommentLike

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

PROF_PIC_ROOT = settings.MEDIA_ROOT + '/profile_pictures'


class ModelTestCase(TestCase):
    def generate_user(self, user_name):
        return User.objects.create(
            username=user_name, password='1', first_name='John', last_name='Doe', email="jd@jd.com"
        )

    def generate_status_post(self, user):
        status_post = StatusPost.objects.create(user=user, text='Lorem ipsum, blah, blah, blah')
        return status_post

    def generate_status_comment(self, post, user):
        status_comment = StatusComment.objects.create(user=user, status_post=post,
                                                      text='Lorem ipsum, blah')
        return status_comment


class StatusPostTest(ModelTestCase):

    def test_saving_and_retrieving_status_posts(self):
        user1 = self.generate_user('woo')
        user2 = self.generate_user('yoo')

        StatusPost.objects.create(user=user2, text='I am so amazed at how much I love this site!')
        StatusPost.objects.create(user=user1, text='The Social Network is soooooooo cool! Wooo!')

        saved_posts = StatusPost.objects.all()
        self.assertEqual(saved_posts.count(), 2)

        first_saved_post = saved_posts[0]
        second_saved_post = saved_posts[1]
        self.assertEqual(first_saved_post.text, 'The Social Network is soooooooo cool! Wooo!')
        self.assertEqual(second_saved_post.text, 'I am so amazed at how much I love this site!')
        self.assertEqual(first_saved_post.user, user1)
        self.assertEqual(second_saved_post.user, user2)

    def test_cannot_save_empty_status_posts(self):
        post = StatusPost(text='')
        with self.assertRaises(ValidationError):
            bob = self.generate_user('bob')
            post.user = bob
            post.save()
            post.full_clean()


class StatusCommentTest(ModelTestCase):

    def test_saving_and_retrieving_status_comments(self):
        user1 = self.generate_user('woo')
        user2 = self.generate_user('yoo')
        status_post = self.generate_status_post(user1)

        StatusComment.objects.create(user=user2, status_post=status_post,
                                     text='Lorem impsum, blah, blah')
        StatusComment.objects.create(user=user1, status_post=status_post,
                                     text='Lorem impsum, blah')

        saved_comments = StatusComment.objects.all()
        self.assertEqual(saved_comments.count(), 2)

        first_saved_comment = saved_comments[0]
        second_saved_comment = saved_comments[1]
        self.assertEqual(first_saved_comment.text, 'Lorem impsum, blah, blah')
        self.assertEqual(second_saved_comment.text, 'Lorem impsum, blah')
        self.assertEqual(first_saved_comment.status_post, status_post)
        self.assertEqual(second_saved_comment.status_post, status_post)
        self.assertEqual(first_saved_comment.user, user2)
        self.assertEqual(second_saved_comment.user, user1)

    def test_cannot_save_empty_status_comments(self):
        comment = StatusComment(text='')
        with self.assertRaises(ValidationError):
            bob = self.generate_user('bob')
            comment.user = bob
            comment.status_post = self.generate_status_post(bob)
            comment.save()
            comment.full_clean()


class PostLikeTest(ModelTestCase):

    def test_saving_and_retrieving_post_likes(self):
        user1 = self.generate_user('user1')
        user2 = self.generate_user('user2')
        post1 = self.generate_status_post(user=user1)
        post2 = self.generate_status_post(user=user2)

        PostLike.objects.create(status_post=post1, user=user1)
        PostLike.objects.create(status_post=post1, user=user2)
        PostLike.objects.create(status_post=post2, user=user1)
        PostLike.objects.create(status_post=post2, user=user2)

        self.assertEqual(PostLike.objects.all().count(), 4)
        self.assertEqual(PostLike.objects.filter(status_post=post1).count(), 2)
        self.assertEqual(PostLike.objects.filter(status_post=post2).count(), 2)
        self.assertEqual(PostLike.objects.filter(user=user1).count(), 2)
        self.assertEqual(PostLike.objects.filter(user=user2).count(), 2)


class CommentLikeTest(ModelTestCase):

    def test_saving_and_retrieving_post_likes(self):
        user1 = self.generate_user('user1')
        user2 = self.generate_user('user2')
        the_post = self.generate_status_post(user=user1)
        comment1 = self.generate_status_comment(post=the_post, user=user1)
        comment2 = self.generate_status_comment(post=the_post, user=user2)

        CommentLike.objects.create(status_comment=comment1, user=user1)
        CommentLike.objects.create(status_comment=comment1, user=user2)
        CommentLike.objects.create(status_comment=comment2, user=user1)
        CommentLike.objects.create(status_comment=comment2, user=user2)

        self.assertEqual(CommentLike.objects.all().count(), 4)
        self.assertEqual(CommentLike.objects.filter(status_comment=comment1).count(), 2)
        self.assertEqual(CommentLike.objects.filter(status_comment=comment2).count(), 2)
        self.assertEqual(CommentLike.objects.filter(user=user1).count(), 2)
        self.assertEqual(CommentLike.objects.filter(user=user2).count(), 2)
