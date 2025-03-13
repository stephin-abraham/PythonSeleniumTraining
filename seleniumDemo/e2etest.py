import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)
driver.find_element(By.XPATH,"//*[text()='Shop']").click()

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "iphone X":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@class='btn btn-success']").click()
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//*[@value='Purchase']").click()
time.sleep(3)
