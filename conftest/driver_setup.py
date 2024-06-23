from configparser import RawConfigParser

import pytest
from selenium import webdriver

from page_objects.sign_In_page import SignIn

config = RawConfigParser()
config.read("/home/renuka/PycharmProjects/selenium_python_testing/settings.ini")


@pytest.fixture
def driver_setup():
    driver = webdriver.Chrome()
    signIn = SignIn(driver)
    signIn.get_url("https://ccms-portal.qa.card91.in/")
    driver.maximize_window()
    signIn.mobile_input(config['Credentials']['mobile_no_corporate'])
    signIn.otp_input(config['Credentials']['OTP'])
    signIn.sign_in_button()
    yield driver
    driver.quit()
