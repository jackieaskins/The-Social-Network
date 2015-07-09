from .base import FunctionalTest

from registration.users import UserModel


class NewVisitorTest(FunctionalTest):

    def test_users_can_fill_out_registration_form_and_are_redirected(self):
        # Tired of Twitter, Facebook, and Instagram Brad has luckily heard
        # about the new social network on the block so he visits the website in
        # his browser
        self.browser.get(self.live_server_url)

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
                            ('email', 'tsnthesocialnetwork@gmail.com'),
                            ('password1', 'bradiscool'),
                            ('password2', 'bradiscool\n')]:
            self.browser.find_element_by_name(name).send_keys(value)

        # He finds himself on another page telling him to activate his account
        p_text = self.browser.find_element_by_tag_name('p').text
        self.assertEquals('Please check your email to complete the registration process.', p_text)

    def test_registered_users_can_view_posts(self):

        # Sally is already a user of The Social Network (go Sally!)
        UserModel().objects.create_user(first_name='Sally',
                                        last_name='Hayes',
                                        username='sally',
                                        email='sally@127.0.0.1:8081',
                                        password='sallyiscooler')

        # Since TSN is so awesome, Sally comes to login as she does almost
        # every day
        self.browser.get(self.live_server_url + '/accounts/login')
        self.browser.find_element_by_name('username').send_keys('sally')
        self.browser.find_element_by_name('password').send_keys('sallyiscooler\n')

        # She is returned to the home page
        self.assertEqual(self.browser.current_url, self.live_server_url + '/')

        # There is a box that she can type into
        postbox = self.browser.find_element_by_id('new_post')
        self.assertEqual(
            postbox.get_attribute('placeholder'),
            "Tell us what's happening!"
        )

        # She enters some text into the post box and presses enter
        postbox.send_keys('TSN is actually the best...\n')
