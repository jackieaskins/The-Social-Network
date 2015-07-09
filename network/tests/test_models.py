from django.contrib.auth import get_user_model
from django.test import TestCase

from network.models import StatusPost


class StatusPostTest(TestCase):

    def test_saving_and_retrieving_status_posts(self):
        User = get_user_model()
        user1 = User.objects.create(
            username='woo', password='123', first_name='John', last_name='Sky', email='woo@woo.com'
        )
        user2 = User.objects.create(
            username='yoo', password='123', first_name='Alex', last_name='Sun', email='yoo@yoo.com'
        )

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
