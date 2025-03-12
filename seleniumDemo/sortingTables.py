import time

from selenium import webdriver
from selenium.webdriver.common.by import By

sortedVeggiesName = []

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on the header name
driver.find_element(By.XPATH,"//*[text()='Veg/fruit name']").click()
# collect all vegetable names
veggiesWebElement = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggiesWebElement:
    sortedVeggiesName.append(ele.text)

# Make a copy before sorting
orginalSortedVeggies = sortedVeggiesName.copy()

# Sort the copied list
sortedVeggiesName.sort()

# Assert that the sorted list matches the displayed sorted order
assert sortedVeggiesName == orginalSortedVeggies
print(orginalSortedVeggies)
time.sleep(3)