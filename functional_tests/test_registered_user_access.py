from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .base import FunctionalTest
from notifications.models import Notification


class ReturningVisitorTest(FunctionalTest):

    def test_registered_users_can_post_comment_and_like(self):

        # Sally is already a user of The Social Network (go Sally!) Since TSN
        # is so awesome, Sally comes to login
        self.login()

        # She is returned to the home page
        self.assertEqual(self.browser.current_url, self.live_server_url + '/')

        # There is a box that she can type into
        postbox = self.browser.find_element_by_id('new_post')
        self.assertEqual(
            postbox.get_attribute('placeholder'),
            "Tell us what's happening!"
        )

        # She enters some text into the post box and presses enter
        postbox.send_keys('TSN is actually the best...\t\n')

        # Her post now appears on the page
        post = self.browser.find_element_by_class_name('status_post')
        self.assertIn('TSN is actually the best...', post.text)

        # Sally sees that her post has 0 likes and shoots her post a like
        self.assertIn('0 people like this',
                      self.browser.find_element_by_class_name('post_likes').text)
        self.browser.find_element_by_class_name('like_status_btn').click()

        # Her post now has one like and the button now reads Unlike
        self.assertIn('1 person likes this',
                      self.browser.find_element_by_class_name('post_likes').text)
        self.assertIn('Unlike', self.browser.find_element_by_class_name('like_status_btn').text)

        # Sally's feeling a little overzealous and decides to comment on her
        # own post
        self.browser.find_element_by_class_name('show_comment_box').click()
        commentbox = self.browser.find_element_by_class_name('new_comment')
        commentbox.send_keys('WOW, COMMENTS TOO?\t\n')

        # After posting, she finds that her comment is on the page
        comment = self.browser.find_element_by_class_name('status_comment')
        self.assertIn('WOW, COMMENTS TOO?', comment.text)

        # So of course, she likes this comment too
        self.browser.find_element_by_class_name('like_comment_btn').click()

        # The comment's got a like now and the button says Unlike
        self.assertIn('1 like', self.browser.find_element_by_class_name('comment_likes').text)
        self.assertIn('Unlike', self.browser.find_element_by_class_name('like_comment_btn').text)

        # Sally is so impressed that she decides to make another post
        # explaining just how impressed she is
        postbox = self.browser.find_element_by_id('new_post')
        postbox.send_keys('I AM SOOOOOO IMPRESSED\t\n')

        # Again, her post appears on the page, above the other post
        self.browser.implicitly_wait(3)
        posts = self.browser.find_elements_by_class_name('status_post')
        self.assertIn('I AM SOOOOOO IMPRESSED', posts[0].text)

    def test_registered_users_can_view_their_own_profile(self):

        # Sally's back and she's logging in again
        self.login()

        # She decides that she wants to check out her profile now and clicks
        # the 'My Profile' link in the navigation bar
        self.browser.implicitly_wait(3)
        self.browser.find_element_by_id('my_profile').click()

        # She sees that her username is in the website url
        self.assertIn('sally', self.browser.current_url)

        # She also notices that her full name, age, birthday, and gender appear
        # on the page
        page_source = self.browser.page_source
        for value in ['Your Profile', 'Sally Hayes', 'Age:', 'Female', 'July 22, 1985']:
            self.assertIn(value, page_source)

    def test_registered_users_can_view_their_own_notifications(self):

        # Sally logs in and notices that she doesn't have any notifications
        self.login()
        num_nots = self.browser.find_element_by_id('num_nots')
        self.assertEqual('', num_nots.text)

        # Somewhere else an old friend of Sally's decides to send her a friend request
        sally = User.objects.get(username='sally')
        Notification.objects.create(
            user=sally,
            notification_type='Friend Request',
            content='Old Friend wants to be your friend.'
        )

        # Sally loads the homepage again and this time she has a notification
        self.browser.get(self.live_server_url + reverse('home'))
        num_nots = self.browser.find_element_by_id('num_nots')
        self.assertEqual('1', num_nots.text)

        # Sally clicks on the notification link to view her new notification
        self.browser.find_element_by_id('my_notifications').click()
        self.assertIn('/notifications/', self.browser.current_url)

        # She clicks on her new notification and sees that the badge displaying
        # her 1 new notification has disappeared
        self.browser.find_element_by_class_name('panel').click()
        self.browser.implicitly_wait(3)
        num_nots = self.browser.find_element_by_id('num_nots')
        self.assertEqual('', num_nots.text)
