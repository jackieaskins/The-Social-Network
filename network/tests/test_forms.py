from django.test import TestCase

from ..forms import StatusPostForm, StatusCommentForm

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class StatusPostFormTest(TestCase):

    def test_form_renders_status_post_text_input(self):
        form = StatusPostForm()
        self.assertIn('placeholder="Tell us what&#39;s happening!"', form.as_p())


class StatusCommentFormTest(TestCase):

    def test_form_renders_status_comment_text_input(self):
        form = StatusCommentForm()
        self.assertIn('placeholder="Did you want to add something?"', form.as_p())
