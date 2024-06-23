import time
from configparser import RawConfigParser

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class OnboardCorporate:

    def __init__(self, driver):
        self.driver = driver
        self.corporate_tab = (By.XPATH, "(//span[normalize-space()='Corporate'])[1]")
        self.onboard_corporate = (By.XPATH, "//button[normalize-space()='Onboard Corporate']")
        self.company_name = (By.XPATH, "//input[@id='companyName']")
        self.company_description = (By.XPATH, "//textarea[@id='companyDescription']")
        self.company_logo = (By.XPATH, "//i[@class='fe fe-camera']")
        self.logo_file = (By.CSS_SELECTOR, "input[type='file']")
        self.GST_number = (By.XPATH, "(//input[@id='gst'])[1]")
        self.PAN_number = (By.XPATH, "(//input[@id='pan'])[1]")
        self.approved_limit = (By.XPATH, "//input[@id='approvedLimit']")
        self.security_type = (By.XPATH, "(//div[@class=' css-19bb58m'])[1]")
        self.security_type_option = (By.XPATH, "//div[@class=' css-1nmdiq5-menu']")
        self.security_number = (By.XPATH, "//input[@id='securityNumber']")
        self.security_amount = (By.XPATH, "//input[@id='securityAmount']")
        self.address1 = (By.XPATH, "//input[@id='addressOne']")
        self.address2 = (By.XPATH, "//input[@id='addressTwo']")
        self.city = (By.XPATH, "//input[@id='city']")
        self.state = (By.XPATH, "//input[@id='state']")
        self.pincode = (By.XPATH, "//input[@id='pincode']")
        self.admin_name = (By.XPATH, "//input[@id='adminName']")
        self.admin_mobile = (By.XPATH, "//input[@id='adminMobile']")
        self.admin_email = (By.XPATH, "//input[@id='adminEmail']")
        self.submit = (By.XPATH, "//div[text()='Submit']")
        self.mobile_field = (By.CSS_SELECTOR, "div[id='row-0'] div[id='cell-3-undefined'] div:nth-child(2)")
        self.card_program = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium fs-5 "
                                       "text-primary css-vubbuv'])[1]")
        self.success_msg = (By.XPATH, "//div[contains(text(),'Success')]")
        self.form_body = (By.XPATH, "//form[@id='corporateOnboardingForm']")

    def click_corporate_tab(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.corporate_tab)).click()
        except TimeoutException:
            print("Timeout occurred while waiting for the corporate tab to be visible")

    def onboard_corporate_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.onboard_corporate)).click()
        except TimeoutException:
            print("Timeout occurred while waiting for the corporate button to be visible")

    def company_name_input(self, name):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.company_name)).send_keys(name)
        except TimeoutException:
            print("Timeout occurred while waiting for the company name to be visible")

    def company_desc_input(self, desc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.company_description)).send_keys(
                desc)
        except TimeoutException:
            print("Timeout occurred while waiting for the company desc to be visible")

    def company_logo_upload(self, filepath):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.logo_file)).send_keys(filepath)
        except TimeoutException:
            print("Timeout occurred while waiting for the company logo to be present in DOM")

    def gst_number_input(self, gst_number):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.GST_number)).send_keys(
                gst_number)
        except TimeoutException:
            print("Timeout occurred while waiting for the GST field to be visible")

    def pan_number_input(self, pan_number):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PAN_number)).send_keys(
                pan_number)
        except TimeoutException:
            print("Timeout occurred while waiting for the PAN field to be visible")

    def approved_limit_input(self, limit):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.approved_limit)).send_keys(
                limit)
        except TimeoutException:
            print("Timeout occurred while waiting for the approve limit field to be visible")

    def security_type_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.security_type))
        element.click()
        # hidden_div = self.driver.execute_script("return document.querySelector('input[name='securityType']")
        # self.driver.execute_script("arguments[0].value = 'FD'", hidden_div)
        option_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.security_type_option))
        option_element.click()
        return option_element

    def security_number_input(self, number):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.security_number)).send_keys(number)
        except TimeoutException:
            print("Timeout occurred while waiting for the security number field to be visible")

    def security_amount_input(self, number):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.security_amount)).send_keys(number)
        except TimeoutException:
            print("Timeout occurred while waiting for the security amount to be visible")

    def address_one(self, address):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.address1)).send_keys(address)
        except TimeoutException:
            print("Timeout occurred while waiting for the address field to be visible")

    def address_two(self, address):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.address2)).send_keys(address)
        except TimeoutException:
            print("Timeout occurred while waiting for the address field to be visible")

    def city_input(self, city):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.city)).send_keys(city)
        except TimeoutException:
            print("Timeout occurred while waiting for the city field to be visible")

    def state_input(self, state):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.state)).send_keys(state)
        except TimeoutException:
            print("Timeout occurred while waiting for the state field to be visible")

    def pincode_input(self, pincode):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.pincode)).send_keys(pincode)
        except TimeoutException:
            print("Timeout occurred while waiting for the pincode field to be visible")

    def admin_name_input(self, admin_name):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.admin_name)).send_keys(admin_name)
        except TimeoutException:
            print("Timeout occurred while waiting for the admin name field to be visible")

    def admin_mobile_input(self, mobile_number):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.admin_mobile)).send_keys(
                mobile_number)
        except TimeoutException:
            print("Timeout occurred while waiting for the admin mobile field to be visible")

    def admin_email_input(self, email):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.admin_email)).send_keys(email)
        except TimeoutException:
            print("Timeout occurred while waiting for the admin email field to be visible")

    def click_submit_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.submit)).click()
        except TimeoutException:
            print("Timeout occurred while waiting for the submit button to be clickable")

    def remove_focus(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.form_body)).click()

    def get_success_msg(self):
        msg = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_msg)).text
        return msg

    def get_mobile_no(self):
        self.driver.refresh()
        mobile_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.mobile_field)).text
        print(mobile_text)
        return mobile_text

    def clear_field(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.pincode))
        element.clear()

    def switch_to_new_window(self):
        all_handles = self.driver.window_handles
        print(len(all_handles))
        new_window_handle = [handle for handle in all_handles if handle != self.driver.current_window_handle][-1]
        self.driver.switch_to.window(new_window_handle)
        time.sleep(5)

    @staticmethod
    def get_mobile_corp():
        config = RawConfigParser()
        config.read("/home/renuka/PycharmProjects/selenium_python_testing/settings.ini")
        print(config.sections())
        print(config["Credentials"]["mobile_no"])
