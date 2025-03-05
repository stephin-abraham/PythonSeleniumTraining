import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome Driver services Selenium
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/otp")
print(driver.title)
print(driver.current_url)
time.sleep(3)
driver.find_element(By.ID,"name").send_keys("stephin")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("stephin123.com")
time.sleep(3)


