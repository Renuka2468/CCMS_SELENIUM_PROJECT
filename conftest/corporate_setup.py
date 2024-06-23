from configparser import RawConfigParser

import pytest
from selenium import webdriver

from page_objects.corporate_limits_page import CorporateLimits

config = RawConfigParser()
config.read("/home/renuka/PycharmProjects/selenium_python_testing/settings.ini")


@pytest.fixture(scope="function")
def driver_setup_corporate():
    driver = webdriver.Chrome()
    corporate_limit = CorporateLimits(driver)
    corporate_limit.get_url("https://ccms-corporate-portal.qa.card91.in/")
    driver.maximize_window()
    corporate_limit.mobile_number_input(config['Credentials']['mobile_no_corporate'])
    corporate_limit.otp_input(config['Credentials']['OTP'])
    corporate_limit.click_signIn()
    driver.implicitly_wait(5)
    corporate_limit.bulk_upload_tab()
    yield driver
    driver.quit()
