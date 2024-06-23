import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CorporateLimits:
    config = configparser.RawConfigParser()
    config.read('settings.ini')

    def __init__(self, driver):
        self.driver = driver
        self.corporate_mobile = (By.XPATH, "//input[@id='formEmail']")
        self.corporate_otp = (By.XPATH, "//div[contains(@class,'pincode-input-container')]//input[1]")
        self.signin = (By.XPATH, "//button[normalize-space()='Sign In']")
        self.bulk_upload = (By.XPATH, "//span[normalize-space()='Bulk Upload']")
        self.upload_drop_down = (By.XPATH, "(//div[@class=' css-19bb58m'])[1]")
        self.upload_option = (By.XPATH, "//div[@class=' css-1nmdiq5-menu']")
        self.sample_corporate_limit_file = (By.XPATH, "//span[normalize-space()='Download Corporate Limits Sample "
                                                      "File']")
        self.sample_corporate_customer_file = (By.XPATH, "//a[@aria-label='download sample file']")
        self.upload_corporate_limit_button = (By.XPATH, "//button[@class='sc-jxOSlx bphwTE btn btn-primary']")
        self.select_corporate_customer_file_input = (By.XPATH, "//input[@class='sc-lcIPJg hjRTUT form-control']")
        self.select_corporate_limit_file_input = (By.XPATH, "//input[@type='file']")
        self.corporate_limit_file_upload = (By.XPATH, "//button[@class='undefined position-relative btn btn-primary']")

    def get_url(self, url):
        self.driver.get(url)

    def mobile_number_input(self, mobile):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.corporate_mobile)).send_keys(mobile)

    def otp_input(self, otp):
        for i in range(1, 7):
            xpath = (By.XPATH, f"//div[contains(@class,'pincode-input-container')]//input[{i}]")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath)).send_keys(otp)

    def click_signIn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.signin)).click()

    def bulk_upload_tab(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.bulk_upload)).click()

    def get_drop_down(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.upload_drop_down)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.upload_option)).click()

    def download_corporate_limit_sample_file(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sample_corporate_limit_file)).click()

    def upload_input_file(self, filepath):
        (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.select_corporate_limit_file_input))
         .send_keys(filepath))
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.corporate_limit_file_upload))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def download_corporate_customer_sample_file(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sample_corporate_customer_file)).click()

    def upload_corporate_customer(self, filepath):
        (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.select_corporate_limit_file_input))
         .send_keys(filepath))
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.corporate_limit_file_upload))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
