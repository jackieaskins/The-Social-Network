from django.test import LiveServerTestCase

from selenium import webdriver

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
