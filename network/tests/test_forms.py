from django.test import TestCase

from network.forms import StatusPostForm


class StatusPostFormTest(TestCase):

    def test_form_renders_status_post_text_input(self):
        form = StatusPostForm()
        self.assertIn('placeholder="Tell us what&#39;s happening!"', form.as_p())
