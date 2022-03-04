import time
from selenium import webdriver
import unittest

from project.Page.signupPage import SignUp

class SignupTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_signup(self):
        driver = self.driver
        driver.get('https://www.amazon.com/')

        sign_up = SignUp(driver)
        sign_up.signup()
        sign_up.fill_name('Safira A')
        sign_up.fill_email('+6287886177686')
        # password not shown due to security
        sign_up.fill_password('******')
        sign_up.fill_repassword('*****')
        sign_up.next_step()

        # we can't bypass captcha and otp, so we should to stop automation for a while
        driver.implicitly_wait(180)