import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
driver.find_element(By.LINK_TEXT,'Click Here').click()
newWindow = driver.window_handles
driver.switch_to.window(newWindow[1])
time.sleep(3)
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(newWindow[0])
time.sleep(2)
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
