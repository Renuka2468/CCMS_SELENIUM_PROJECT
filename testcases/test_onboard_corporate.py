from configparser import RawConfigParser

import pytest

from page_objects.onboard_corporate_page import OnboardCorporate
from conftest.onboard_setup import onboard_setup
from page_objects.error_page import CorporateOnboardError
from utils.onCorp_error_msg import ErrorMsg
from utils.random_data_generator import random_generator

test_data_positive = [
    {"company_name": "card91", "company_desc": "This is business for providing card backend compatibility",
     "company_logo": "/home/renuka/Downloads/Notes.pdf",
     "gst_number": random_generator.get_gst_number(), "pan_number": random_generator.get_pan_number(),
     "approved_limit": "1000000",
     "security_number": "9874", "security_amount": "10000000", "address_1": random_generator.get_address(),
     "address_2": random_generator.get_address(), "city": random_generator.get_city(),
     "state": random_generator.get_state(),
     "pincode": random_generator.get_pincode(), "admin_name": "denver", "mobile_no": random_generator.get_mobile(),
     "email": random_generator.get_email()},
    {"company_name": "Card91 ltd", "company_desc": "This is business for providing card backend compatibility",
     "company_logo": "/home/renuka/PycharmProjects/selenium_python_testing/uploads/logo.jpg",
     "gst_number": random_generator.get_gst_number(), "pan_number": random_generator.get_pan_number(),
     "approved_limit": "1000000",
     "security_number": "9874", "security_amount": "10000000", "address_1": random_generator.get_address(),
     "address_2": random_generator.get_address(), "city": random_generator.get_city(),
     "state": random_generator.get_state(),
     "pincode": random_generator.get_pincode(), "admin_name": "denver", "mobile_no": random_generator.get_mobile(),
     "email": random_generator.get_email()},
]

name_data_special_char = [{"company_name": "@1234"}]
name_data_length = [{"company_name": "q"}, {"company_name": "qwertioreuglkjfvfdnjkvdkfuehfhjkcjksbcdbvmbd"}]
description_data_special_char = [{"company_name": "card976", "company_desc": "@google would be good "},
                                 {"company_name": "card976", "company_desc": "this is description, checkers"}]
description_data_length = [{"company_name": "card976", "company_desc": "google"}]
company_logo_test_data = [{"company_name": "card976", "company_desc": "google would be good checkers",
                           "company_logo": "/home/renuka/Downloads/Notes.pdf"},
                          {"company_name": "card976", "company_desc": "google would be good checkers",
                           "company_logo": "/home/renuka/Downloads/download (1).jpeg"}]
gst_number_test_data = [{"company_name": "card976", "company_desc": "google would be good checkers",
                         "company_logo": "/home/renuka/Downloads/download (1).jpeg", "gst_number": "67HGTAF5843A7Z"}]
pan_number_test_data = [{"company_name": "card976", "company_desc": "google would be good checkers",
                         "company_logo": "/home/renuka/Downloads/download (1).jpeg", "gst_number": "67HGTAF5843A7Z",
                         "pan_number": "ABCDE234D"}]
pan_number_test_data_exist = [{"company_name": "card976", "company_desc": "google would be good checkers",
                               "company_logo": "/home/renuka/Downloads/download (1).jpeg",
                               "gst_number": "67HGTAF5843A7Z2", "pan_number": "ABCDE1234D"}]
gst_number_test_data_exist = [{"company_name": "card976", "company_desc": "google would be good checkers",
                               "company_logo": "/home/renuka/Downloads/download (1).jpeg",
                               "gst_number": "67HGTAF5843A7Z5"}]
security_number_test_data_char = [{"company_name": "card91",
                                   "company_desc": "This is business for providing card backend compatibility",
                                   "company_logo": "/home/renuka/PycharmProjects/selenium_python_testing/uploads/logo"
                                                   ".jpg",
                                   "gst_number": random_generator.get_gst_number(),
                                   "pan_number": random_generator.get_pan_number(),
                                   "security_number": "abcder"}]
address_test_data_length = [{"address_1": "we", "address_2": "as"},
                            {"address_1": "weryuiocdefguioplkjhnmbvcdq1346790ujdzwfvyik",
                             "address_2": "asqwertyuioplkjhgfdsazxcvbnmkjuiopwe456891245"}]
city_state_test_data_length = [{"city": "we", "state": "as"},
                               {"city": "weryuiocdefguioplkjhnmbvcdq1346790ujdzwfvyik",
                                "state": "asqwertyuioplkjhgfdsazxcvbnmkjuiopwe456891245"}]
pincode_test_data_length = [{"pincode": "  "}, {"pincode": "124"}, {"pincode": "uehfjkd"}]
pincode_error_test_data = [{"error_valid": ErrorMsg.ENTER_VALID_PINCODE_ERROR},
                           {"error_valid": ErrorMsg.ENTER_VALID_PINCODE_ERROR},
                           {"error_valid": ErrorMsg.ENTER_VALID_PINCODE_ERROR}]
admin_name_special_char_blank = [{"company_name": "card91",
                                  "company_desc": "This is business for providing card backend compatibility",
                                  "company_logo": "/home/renuka/Downloads/Notes.pdf",
                                  "gst_number": random_generator.get_gst_number(),
                                  "pan_number": random_generator.get_pan_number(),
                                  "security_number": "9874", "security_amount": "10000000",
                                  "address_1": random_generator.get_address(),
                                  "address_2": random_generator.get_address(), "city": random_generator.get_city(),
                                  "state": random_generator.get_state(),
                                  "pincode": random_generator.get_pincode(), "admin_name": "denver's"},
                                 {"company_name": "card91",
                                  "company_desc": "This is business for providing card backend compatibility",
                                  "company_logo": "/home/renuka/Downloads/Notes.pdf",
                                  "gst_number": random_generator.get_gst_number(),
                                  "pan_number": random_generator.get_pan_number(),
                                  "security_number": "9874", "security_amount": "10000000",
                                  "address_1": random_generator.get_address(),
                                  "address_2": random_generator.get_address(), "city": random_generator.get_city(),
                                  "state": random_generator.get_state(),
                                  "pincode": random_generator.get_pincode(), "admin_name": "       "}]
mobile_test_data_length = [{"mobile_no": "94837"}, {"mobile_no": "whdj123"}]
mobile_error_msg = [{"mobile_error": ErrorMsg.MOBILE_NUMBER_MUST_BE_OF_10_DIGITS_ERROR},
                    {"mobile_error": ErrorMsg.ENTER_VALID_MOBILE_NUMBER_ERROR}]
approved_limit_test_data = [{"approve_limit": "10000"}, {"approve_limit": "10000000000000"}]
approved_limit_error_msg = [{"limit_err": ErrorMsg.MIN_APPROVED_LIMIT_IS_RS_10_LAKHS_ERROR},
                            {"limit_err": ErrorMsg.MAX_APPROVED_LIMIT_CANNOT_EXCEED_RS_100_CRORES_ERROR}]

config = RawConfigParser()
config.read("/home/renuka/PycharmProjects/selenium_python_testing/settings.ini")


@pytest.mark.usefixtures("onboard_setup")
class TestCorporateOnboard:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", test_data_positive)
    def test_onboard_corporate_success(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        assert "Card91 - Corporate" in driver.title
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.company_logo_upload(data["company_logo"])
        onboardCorporate.gst_number_input(data["gst_number"])
        onboardCorporate.pan_number_input(data["pan_number"])
        onboardCorporate.approved_limit_input(data["approved_limit"])
        onboardCorporate.security_type_dropdown()
        onboardCorporate.security_number_input(data["security_number"])
        onboardCorporate.security_amount_input(data["security_amount"])
        onboardCorporate.address_one(data["address_1"])
        onboardCorporate.address_two(data["address_2"])
        onboardCorporate.city_input(data["city"])
        onboardCorporate.state_input(data["state"])
        onboardCorporate.pincode_input(data["pincode"])
        onboardCorporate.admin_name_input(data["admin_name"])
        onboardCorporate.admin_mobile_input(data["mobile_no"])
        onboardCorporate.admin_email_input(data["email"])
        onboardCorporate.click_submit_button()
        success_msg = onboardCorporate.get_success_msg()
        assert success_msg == "Success"

    def test_all_mandatory_fields_error(self, onboard_setup):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.click_submit_button()
        name_error = corporate_error.get_company_name_error()
        desc_error = corporate_error.get_company_desc_error()
        logo_error = corporate_error.get_company_logo_error()
        gst_error = corporate_error.get_gst_number_error()
        pan_error = corporate_error.get_pan_number_error()
        approved_limit_error = corporate_error.get_approved_limit_error()
        security_type_error = corporate_error.get_security_type_error()
        security_number_error = corporate_error.get_security_number_error()
        security_amount_error = corporate_error.get_security_amount_error()
        address_error = corporate_error.get_address_1_error()
        city_error = corporate_error.get_city_error()
        state_error = corporate_error.get_state_error()
        pincode_error = corporate_error.get_pincode_error()
        admin_name_error = corporate_error.get_admin_name_error()
        mobile_no_error = corporate_error.get_mobile_no_error()
        email_error = corporate_error.get_email_error()
        assert name_error == ErrorMsg.COMPANY_NAME_IS_REQUIRED_ERROR
        assert desc_error == ErrorMsg.COMPANY_DESCRIPTION_IS_REQUIRED_ERROR
        assert logo_error == ErrorMsg.COMPANY_LOGO_IS_REQUIRED_ERROR
        assert gst_error == ErrorMsg.ENTER_GST_NUMBER_ERROR
        assert pan_error == ErrorMsg.ENTER_PAN_NUMBER_ERROR
        assert approved_limit_error == ErrorMsg.APPROVED_LIMIT_IS_REQUIRED_ERROR
        assert security_type_error == ErrorMsg.SECURITY_TYPE_IS_REQUIRED_ERROR
        assert security_number_error == ErrorMsg.SECURITY_NUMBER_IS_REQUIRED_ERROR
        assert security_amount_error == ErrorMsg.SECURITY_AMOUNT_IS_REQUIRED_ERROR
        assert address_error == ErrorMsg.ENTER_ADDRESS_LINE_1_ERROR
        assert city_error == ErrorMsg.ENTER_CITY_ERROR
        assert state_error == ErrorMsg.ENTER_STATE_ERROR
        assert pincode_error == ErrorMsg.ENTER_PINCODE_ERROR
        assert admin_name_error == ErrorMsg.ADMIN_NAME_IS_REQUIRED_ERROR
        assert mobile_no_error == ErrorMsg.ADMIN_MOBILE_IS_REQUIRED_ERROR
        assert email_error == ErrorMsg.ADMIN_EMAIL_IS_REQUIRED_ERROR

    @pytest.mark.parametrize("data", test_data_positive)
    def test_existing_corporate(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.company_logo_upload(data["company_logo"])
        onboardCorporate.gst_number_input(data["gst_number"])
        onboardCorporate.pan_number_input(data["pan_number"])
        onboardCorporate.approved_limit_input(data["approved_limit"])
        onboardCorporate.security_type_dropdown()
        onboardCorporate.security_number_input(data["security_number"])
        onboardCorporate.security_amount_input(data["security_amount"])
        onboardCorporate.address_one(data["address_1"])
        onboardCorporate.address_two(data["address_2"])
        onboardCorporate.city_input(data["city"])
        onboardCorporate.state_input(data["state"])
        onboardCorporate.pincode_input(data["pincode"])
        onboardCorporate.admin_name_input(data["admin_name"])
        onboardCorporate.admin_mobile_input(config["Credentials"]["mobile_no_existing"])
        onboardCorporate.admin_email_input(data["email"])
        onboardCorporate.click_submit_button()
        popup_error = corporate_error.get_exist_mobile_corporate_error()
        assert popup_error == ErrorMsg.ADMIN_WITH_THIS_MOBILE_NUMBER_EXISTS_ERROR

    @pytest.mark.parametrize("data", name_data_special_char)
    def test_company_name_special_char(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_company_name_error()
        assert error == ErrorMsg.PLEASE_ENTER_VALID_COMPANY_NAME_ERROR

    @pytest.mark.parametrize("data", name_data_length)
    def test_company_name_length(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_company_name_error()
        assert error == ErrorMsg.COMPANY_NAME_MUST_BE_BETWEEN_3_42_CHARACTERS_ERROR

    @pytest.mark.parametrize("data", description_data_special_char)
    def test_company_desc_special_char(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_company_desc_error()
        assert error == ErrorMsg.PLEASE_ENTER_VALID_COMPANY_DESCRIPTION_ERROR

    @pytest.mark.parametrize("data", description_data_length)
    def test_company_desc_length(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_company_desc_error()
        assert error == ErrorMsg.COMPANY_DESCRIPTION_MUST_BE_BETWEEN_10_150_CHARACTERS_ERROR

    @pytest.mark.parametrize("data", company_logo_test_data)  #.jpg,.jpeg,.png,.webp
    def test_pdf_large_logo(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.company_logo_upload(data["company_logo"])
        onboardCorporate.remove_focus()
        success_msg = onboardCorporate.get_success_msg()
        assert success_msg == "Success"

    @pytest.mark.parametrize("data", gst_number_test_data)
    def test_wrong_GST(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.company_logo_upload(data["company_logo"])
        onboardCorporate.gst_number_input(data["gst_number"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_gst_number_error()
        assert error == ErrorMsg.ENTER_VALID_GST_NUMBER_ERROR

    @pytest.mark.parametrize("data", gst_number_test_data_exist)
    def test_exist_GST(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.company_logo_upload(data["company_logo"])
        onboardCorporate.gst_number_input(data["gst_number"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_gst_number_error()
        assert error == ErrorMsg.PLEASE_ENTER_UNIQUE_GST_NUMBER_ERROR

    @pytest.mark.parametrize("data", pan_number_test_data)
    def test_wrong_PAN(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.company_logo_upload(data["company_logo"])
        onboardCorporate.gst_number_input(data["gst_number"])
        onboardCorporate.pan_number_input(data["pan_number"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_pan_number_error()
        assert error == ErrorMsg.ENTER_VALID_PAN_NUMBER_ERROR

    @pytest.mark.parametrize("data", pan_number_test_data_exist)
    def test_exist_PAN(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.company_logo_upload(data["company_logo"])
        onboardCorporate.gst_number_input(data["gst_number"])
        onboardCorporate.pan_number_input(data["pan_number"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_pan_number_error()
        assert error == ErrorMsg.PLEASE_ENTER_UNIQUE_PAN_NUMBER_ERROR

    @pytest.mark.parametrize("data, expected", zip(approved_limit_test_data, approved_limit_error_msg))
    def test_approved_limit_minmax(self, onboard_setup, data, expected):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.approved_limit_input(data["approve_limit"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_approved_limit_error()
        assert error == expected["limit_err"]

    @pytest.mark.parametrize("data", security_number_test_data_char)
    def test_security_number_char(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.company_name_input(data["company_name"])
        onboardCorporate.company_desc_input(data["company_desc"])
        onboardCorporate.company_logo_upload(data["company_logo"])
        onboardCorporate.gst_number_input(data["gst_number"])
        onboardCorporate.pan_number_input(data["pan_number"])
        onboardCorporate.security_type_dropdown()
        onboardCorporate.security_number_input(data["security_number"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_security_number_error()
        print(error)

    @pytest.mark.parametrize("data", address_test_data_length)
    def test_address_length(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.address_one(data["address_1"])
        onboardCorporate.address_two(data["address_2"])
        onboardCorporate.remove_focus()
        error_address1 = corporate_error.get_address_1_error()
        error_address2 = corporate_error.get_address_2_error()
        assert error_address1 == ErrorMsg.ENTER_ADDRESS_BETWEEN_3_42_CHARACTERS_ERROR
        assert error_address2 == ErrorMsg.ENTER_ADDRESS_BETWEEN_3_42_CHARACTERS_ERROR

    @pytest.mark.parametrize("data", city_state_test_data_length)
    def test_city_state_length(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.city_input(data["city"])
        onboardCorporate.remove_focus()
        error_city = corporate_error.get_city_error()
        onboardCorporate.state_input(data["state"])
        onboardCorporate.remove_focus()
        error_state = corporate_error.get_state_error()
        assert error_city == ErrorMsg.ENTER_CITY_BETWEEN_3_42_CHARACTERS_ERROR
        assert error_state == ErrorMsg.ENTER_STATE_BETWEEN_3_42_CHARACTERS_ERROR

    @pytest.mark.parametrize("data", city_state_test_data_length)
    def test_city_state_length(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.city_input(data["city"])
        onboardCorporate.remove_focus()
        error_city = corporate_error.get_city_error()
        onboardCorporate.state_input(data["state"])
        onboardCorporate.remove_focus()
        error_state = corporate_error.get_state_error()
        assert error_city == ErrorMsg.ENTER_CITY_BETWEEN_3_42_CHARACTERS_ERROR
        assert error_state == ErrorMsg.ENTER_STATE_BETWEEN_3_42_CHARACTERS_ERROR

    @pytest.mark.parametrize("data, expected", zip(pincode_test_data_length, pincode_error_test_data))
    def test_pincode_length_char(self, onboard_setup, data, expected):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.pincode_input(data["pincode"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_pincode_error()
        assert error == expected["error_valid"]

    @pytest.mark.parametrize("data", admin_name_special_char_blank)
    def test_admin_name_special_char(self, onboard_setup, data):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.admin_name_input(data["admin_name"])
        onboardCorporate.remove_focus()
        actual_error = corporate_error.get_admin_name_error()
        assert actual_error == ErrorMsg.PLEASE_ENTER_VALID_ADMIN_NAME_ERROR

    @pytest.mark.parametrize("data, expected", zip(pincode_test_data_length, pincode_error_test_data))
    def test_pincode_length_char(self, onboard_setup, data, expected):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.pincode_input(data["pincode"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_pincode_error()
        onboardCorporate.clear_field()
        assert error == expected["error_valid"]

    @pytest.mark.parametrize("data, expected", zip(mobile_test_data_length, mobile_error_msg))
    def test_mobile_length_char(self, onboard_setup, data, expected):
        driver = onboard_setup
        onboardCorporate = OnboardCorporate(driver)
        corporate_error = CorporateOnboardError(driver)
        onboardCorporate.admin_mobile_input(data["mobile_no"])
        onboardCorporate.remove_focus()
        error = corporate_error.get_mobile_no_error()
        onboardCorporate.clear_field()
        assert error == expected["mobile_error"]

    # @pytest.mark.regression
    # def test_dropdown(self, onboard_setup):
    #     driver = onboard_setup
    #     onboardCorporate = OnboardCorporate(driver)
    #     driver.implicitly_wait(5)
    #     element = onboardCorporate.security_type_dropdown()
    #     time.sleep(4)
    #     assert element.is_enabled()
