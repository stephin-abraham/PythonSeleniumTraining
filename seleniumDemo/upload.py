from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path = "C:/Users/Stephin Philip A/Downloads/download.xlsx"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

driver.find_element(By.XPATH, "//button[@class='button']").click()
file_input = driver.find_element(By.XPATH, '//input[@id="fileinput"]')
file_input.send_keys(file_path)

wait = WebDriverWait(driver,5)
toast_locator = (By.CSS_SELECTOR," .Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)
