from django.test import TestCase

from ..forms import UserProfileForm

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class UserProfileFormTest(TestCase):

    def test_form_renders_status_post_text_input(self):
        form = UserProfileForm()
        self.assertIn('placeholder="Format: mm/dd/YYYY"', form.as_p())
