from django.core.urlresolvers import reverse

from .base import FunctionalTest
from registration.users import UserModel


class NewVisitorTest(FunctionalTest):

    def test_users_can_fill_out_registration_form_and_create_profile(self):
        # Tired of Twitter, Facebook, and Instagram Brad has luckily heard
        # about the new social network on the block so he visits the website in
        # his browser
        self.browser.get(self.live_server_url + reverse('home'))

        # He notices that the title mentions TSN (so much cooler than Twitter
        # or Facebook) AND the page welcomes him to the site
        self.assertIn('TSN', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome', header_text)

        # He sees a link telling him to Register and he clicks it
        self.browser.find_element_by_id('register').click()

        # He winds up on a brand new page
        register_url = self.browser.current_url
        self.assertIn('/accounts/register', register_url)

        # Brad fills out the form on this page to create an account with TSN
        # and presses enter
        for name, value in [('first_name', 'Brad'),
                            ('last_name', 'Pitt'),
                            ('username', 'brad'),
                            ('email', 'bradtheman@btm.com'),
                            ('password1', 'bradiscool'),
                            ('password2', 'bradiscool\t\n')]:
            self.browser.find_element_by_name(name).send_keys(value)

        # He finds himself on another page telling him to activate his account
        p_text = self.browser.find_element_by_tag_name('p').text
        self.assertEquals('Please check your email to complete the registration process.', p_text)

        # After activating, he goes to the login page and logs in
        brad = UserModel().objects.get(username='brad')
        brad.is_active = True
        brad.save()
        self.browser.get(self.live_server_url + reverse('auth_login'))
        self.browser.find_element_by_name('username').send_keys('brad')
        self.browser.find_element_by_name('password').send_keys('bradiscool\t\n')

        # He is then immediately redirected to a page asking him to create a
        # profile
        self.browser.implicitly_wait(3)
        self.assertIn('profile/create', self.browser.current_url)

        # He provides his birthday and his gender
        self.browser.find_element_by_name('birthday').send_keys('12/18/1963')
        self.browser.find_element_by_name('gender').send_keys('M\t\n')

        # He is now on the homepage again, this time he sees a post box
        self.assertEqual(self.live_server_url + reverse('home'), self.browser.current_url)
        self.assertIn('new_post', self.browser.page_source)
