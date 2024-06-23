from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CorporateOnboardError:

    def __init__(self, driver):
        self.driver = driver
        self.company_name = (By.XPATH, "(//div[@class='invalid-feedback'])[1]")
        self.company_desc = (By.XPATH, "(//div[@class='invalid-feedback'])[2]")
        self.company_logo = (By.XPATH, "//div[normalize-space()='Company logo is required']")
        self.gst_number = (By.XPATH, "(//div[@class='invalid-feedback'])[3]")
        self.pan_number = (By.XPATH, "(//div[@class='invalid-feedback'])[4]")
        self.approved_limit = (By.XPATH, "(//div[@class='invalid-feedback'])[5]")
        self.security_type = (By.XPATH, "//div[normalize-space()='Security Type is required']")
        self.security_number = (By.XPATH, "(//div[@class='invalid-feedback'])[6]")
        self.security_amount = (By.XPATH, "(//div[@class='invalid-feedback'])[7]")
        self.address_1 = (By.XPATH, "(//div[@class='invalid-feedback'])[8]")
        self.address_2 = (By.XPATH, "(//div[@class='invalid-feedback'])[9]")
        self.city = (By.XPATH, "(//div[@class='invalid-feedback'])[10]")
        self.state = (By.XPATH, "(//div[@class='invalid-feedback'])[11]")
        self.pincode = (By.XPATH, "(//div[@class='invalid-feedback'])[12]")
        self.admin_name = (By.XPATH, "(//div[@class='invalid-feedback'])[13]")
        self.mobile_no = (By.XPATH, "(//div[@class='invalid-feedback'])[14]")
        self.email = (By.XPATH, "(//div[@class='invalid-feedback'])[15]")
        self.existing_mobile_popoup = (By.XPATH, "//div[contains(text(),'Admin with this mobile number exists')]")
        self.name_desc_field = (By.XPATH, "//div[contains(text(),'An error occurred')]")

    def get_company_name_error(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.company_name))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.text

    def get_company_desc_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.company_desc)).text
        return error

    def get_company_logo_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.company_logo)).text
        return error

    def get_gst_number_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.gst_number)).text
        return error

    def get_pan_number_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.pan_number)).text
        return error

    def get_approved_limit_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.approved_limit)).text
        return error

    def get_security_type_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.security_type)).text
        return error

    def get_security_number_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.security_number)).text
        return error

    def get_security_amount_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.security_amount)).text
        return error

    def get_address_1_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.address_1)).text
        return error

    def get_address_2_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.address_2)).text
        return error

    def get_city_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.city)).text
        return error

    def get_state_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.state)).text
        return error

    def get_pincode_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.pincode)).text
        return error

    def get_admin_name_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.admin_name)).text
        return error

    def get_mobile_no_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.mobile_no)).text
        return error

    def get_email_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email)).text
        return error

    def get_exist_mobile_corporate_error(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.existing_mobile_popoup)).text
        return error

    def get_name_desc_field(self):
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.name_desc_field)).text
        return error
