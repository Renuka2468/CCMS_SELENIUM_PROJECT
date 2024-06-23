import time
from configparser import RawConfigParser

import pytest
from selenium import webdriver

from page_objects.onboard_corporate_page import OnboardCorporate
from page_objects.sign_In_page import SignIn

config = RawConfigParser()
config.read("/home/renuka/PycharmProjects/selenium_python_testing/settings.ini")


@pytest.fixture(scope="function")
def onboard_setup():
    driver = webdriver.Chrome()
    signIn = SignIn(driver)
    onboardCorporate = OnboardCorporate(driver)
    signIn.get_url("https://ccms-portal.qa.card91.in/")
    driver.maximize_window()
    driver.refresh()
    signIn.mobile_input(config['Credentials']['mobile_no_onboard'])
    signIn.otp_input(config['Credentials']['OTP'])
    signIn.sign_in_button()
    onboardCorporate.click_corporate_tab()
    onboardCorporate.onboard_corporate_button()
    yield driver
    driver.quit()
