from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .base import FunctionalTest
from profiles.models import UserProfile
from registration.users import UserModel


class ReturningVisitorTest(FunctionalTest):

    def test_registered_users_can_post_comment_and_like(self):

        # Sally is already a user of The Social Network (go Sally!) Since TSN
        # is so awesome, Sally comes to login
        self.login('sally', 'sallyiscooler')

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
        self.browser.wait.until(lambda x:
                                self.browser.find_element_by_class_name('post_likes').text ==
                                '1 person likes this',
                                '1 person likes this not found in .post_likes')
        self.assertIn('Unlike', self.browser.find_element_by_class_name('like_status_btn').text,)
        self.assertIn('1 person likes this',
                      self.browser.find_element_by_class_name('post_likes').text)

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
        self.login('sally', 'sallyiscooler')

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

    def test_registered_users_can_add_friends_and_accept_friend_requests(self):

        # Sally is back and she's so excited because her best friend Jo Smo has
        # just joined TSN
        jo = UserModel().objects.create_user(username='josmo', first_name='Jo', last_name='Smo',
                                             password='josmoyouknow', email='josmo@holup.com')
        UserProfile.objects.create(user=jo, birthday='1985-03-15', gender='M')
        self.login('sally', 'sallyiscooler')

        # Sally decides goes to view her friends and realizes that she doesn't
        # have any :(
        self.browser.find_element_by_id('my_friends').click()
        self.assertIn("doesn't have any friends", self.browser.page_source)

        # To remedy this, she goes to the find friend page to find Jo
        self.browser.find_element_by_id('find_friends').click()
        self.browser.find_element_by_name('query').send_keys('jo smo\n')

        # Jo Smo appears in her results and she clicks the button to add him
        # as a friend
        self.assertIn('Jo Smo', self.browser.find_element_by_class_name('media-heading').text)
        self.browser.find_element_by_class_name('btn-success').click()

        # The button now reads 'Cancel Request' and is yellow
        self.assertIn('Cancel Request', self.browser.page_source)
        self.assertIn('btn-warning', self.browser.page_source)

        # Since Sally and Jo share a computer Sally logs out and Jo logs in
        self.browser.find_element_by_id('logout').click()
        self.login('josmo', 'josmoyouknow')

        # Jo notices that he has a notification and clicks on the link
        notifications = self.browser.find_element_by_id('my_notifications')
        self.assertIn('1', notifications.text)
        notifications.click()

        # He clicks on the notification on the page and accepts the request
        self.browser.find_element_by_class_name('panel-heading').click()
        self.browser.find_element_by_class_name('btn-success').click()

        # Jo then goes to his friends and sees Sally is one of them
        self.browser.find_element_by_id('my_friends').click()
        self.assertIn('Sally Hayes', self.browser.find_element_by_class_name('media-heading').text)
