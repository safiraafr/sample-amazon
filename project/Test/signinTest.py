from selenium import webdriver
import unittest

from project.Page.signinPage import SignIn

class SignupTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_signup(self):
        driver = self.driver
        driver.get('https://www.amazon.com/')

        sign_in = SignIn(driver)
        sign_in.login()
        sign_in.fill_email('+62')
        sign_in.next_step()
        # password not shown due to security
        sign_in.fill_password('****')
        sign_in.submit()
