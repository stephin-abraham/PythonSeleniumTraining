import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome Driver services Selenium
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
time.sleep(3)
driver.find_element(By.NAME,"name").send_keys("stephin")
driver.find_element(By.XPATH,"//input[@name='email']" ).send_keys("stephin123@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("stephin123")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
drop = driver.find_element(By.ID,"exampleFormControlSelect1")
select =  Select(drop)
select.select_by_visible_text("Male")
driver.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
message= driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
time.sleep(3)


