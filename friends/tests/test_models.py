from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import Friendship


class ModelTestCase(TestCase):
    def generate_user(self, user_name):
        return User.objects.create(
            username=user_name, password='1', first_name='John', last_name='Doe', email="jd@jd.com"
        )


class FriendshipTest(ModelTestCase):

    def test_saving_and_retrieving_friendships(self):
        user1 = self.generate_user('user1')
        user2 = self.generate_user('user2')

        Friendship.objects.create(to_user=user1, from_user=user2)

        friendships = Friendship.objects.all()

        self.assertEqual(friendships.count(), 1)

        self.assertEqual(friendships[0].status, 0)
        self.assertEqual(friendships[0].response_date, None)

        friendship1 = friendships[0]

        friendship1.status = 1
        friendship1.save()

        Friendship.objects.create(to_user=user2, from_user=user1, status=1,
                                  response_date=friendship1.response_date)

        friendships = Friendship.objects.all()
        self.assertEqual(friendships.count(), 2)

        self.assertEqual(friendships[0].status, friendships[1].status)
        self.assertEqual(friendships[0].response_date, friendships[1].response_date)
        self.assertEqual(friendships[0].to_user, friendships[1].from_user)
        self.assertEqual(friendships[0].from_user, friendships[1].to_user)
        self.assertEqual(
            str(friendships[0]),
            '%s to %s' % (friendships[0].from_user.username, friendships[0].to_user.username)
        )

    def test_friendship_error_raising(self):
        user = self.generate_user('user1')

        with self.assertRaises(ValidationError):
            Friendship.objects.create(to_user=user, from_user=user, status=0)
