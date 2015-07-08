from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_must_register_to_access_site(self):
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
