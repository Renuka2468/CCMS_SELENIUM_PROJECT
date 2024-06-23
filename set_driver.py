import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.com")
print(driver.title)
time.sleep(2)
driver.get("https://google.com")
print(driver.title)
time.sleep(2)
driver.quit()