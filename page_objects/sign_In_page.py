from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignIn:

    def __init__(self, driver):
        self.xpath = None
        self.driver = driver
        self.mobile_number_input = (By.XPATH, "//input[@id='formEmail']")
        self.sign_in = (By.XPATH, "//button[normalize-space()='Sign In']")

    def get_url(self, url):
        self.driver.get(url)

    def mobile_input(self, mobile):
        self.driver.find_element(*self.mobile_number_input).send_keys(mobile)

    def otp_input(self, otp):
        try:
            for i in range(1, 7):
                self.xpath = (By.XPATH, f"//div[contains(@class,'pincode-input-container')]//input[{i}]")
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.xpath)).send_keys(otp)
        except TimeoutException:
            print("Timeout occurred while waiting for the PAN field to be visible")

    def sign_in_button(self):
        self.driver.find_element(*self.sign_in).click()
