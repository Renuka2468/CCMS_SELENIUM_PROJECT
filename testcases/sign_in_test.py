import time

import pytest

from page_objects.sign_In_page import SignIn
from conftest.driver_setup import driver_setup


@pytest.fixture
def login(driver_setup):
    driver = driver_setup
    signin = SignIn(driver)
    signin.get_url("https://ccms-portal.qa.card91.in/")
    driver.maximize_window()
    time.sleep(2)
    signin.mobile_input("9888888808")
    time.sleep(2)
    signin.otp_input("1")
    time.sleep(2)
    signin.sign_in_button()
