from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from profiles.models import UserProfile
from registration.users import UserModel

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.wait = WebDriverWait(self.browser, 10)
        sally = UserModel().objects.create_user(
            first_name='Sally',
            last_name='Hayes',
            username='sally',
            email='sally@127.0.0.1:8081',
            password='sallyiscooler'
        )
        sally_profile = UserProfile()
        sally_profile.user = sally
        sally_profile.birthday = '1985-07-22'
        sally_profile.gender = 'F'
        sally_profile.save()

    def tearDown(self):
        self.browser.quit()

    def login(self, username, password):
        self.browser.get(self.live_server_url + '/accounts/login')
        self.browser.find_element_by_name('username').send_keys(username)
        self.browser.find_element_by_name('password').send_keys(password + '\n')
