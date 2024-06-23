import time

from conftest.corporate_setup import driver_setup_corporate
from page_objects.corporate_limits_page import CorporateLimits


def test_corporate_limits(driver_setup_corporate):
    driver = driver_setup_corporate
    corporate_limit = CorporateLimits(driver)
    corporate_limit.mobile_number_input("9616926288")
    corporate_limit.otp_input()
    corporate_limit.click_signIn()
    corporate_limit.bulk_upload_tab()
    corporate_limit.download_corporate_limit_sample_file()
    filepath = "/home/renuka/Downloads/Corporate_Limits_Default_New_renuka_1.csv"
    corporate_limit.upload_input_file(filepath)
    time.sleep(4)


def test_corporate_customer(driver_setup_corporate):
    driver = driver_setup_corporate
    corporate_limit = CorporateLimits(driver)
    corporate_limit.mobile_number_input("9616926288")
    corporate_limit.otp_input()
    corporate_limit.click_signIn()
    corporate_limit.bulk_upload_tab()
    corporate_limit.get_drop_down()
    corporate_limit.download_corporate_customer_sample_file()
    filepath = "/home/renuka/Downloads/Corporate_Customer.csv"
    corporate_limit.upload_corporate_customer(filepath)
    time.sleep(4)
