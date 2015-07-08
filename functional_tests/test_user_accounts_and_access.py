from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_must_register_to_access_site(self):
        # Tired of Twitter, Facebook, and Instagram Brad has luckily heard
        # about the new social network on the block so he types in the website
        # in his browser
        self.browser.get(self.live_server_url)

        # As he is not registered, he winds up on a brand new page
        register_url = self.browser.current_url
        self.assertIn('/accounts/register', register_url)

        # The title and header mention the word 'Register' so Brad understands
        # that's what he's there to do
        self.assertIn('Register', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Register', header_text)
