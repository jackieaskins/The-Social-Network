from django.test import TestCase

from network.forms import StatusPostForm, UserProfileForm

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class StatusPostFormTest(TestCase):

    def test_form_renders_status_post_text_input(self):
        form = StatusPostForm()
        self.assertIn('placeholder="Tell us what&#39;s happening!"', form.as_p())


class UserProfileFormTest(TestCase):

    def test_form_renders_status_post_text_input(self):
        form = UserProfileForm()
        self.assertIn('placeholder="Format: mm/dd/YYYY"', form.as_p())
