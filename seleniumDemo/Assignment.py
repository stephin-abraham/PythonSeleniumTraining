import time
from selenium import webdriver
from selenium.webdriver.common.by import By

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

# Initialize driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Search for items
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(4)  # Allow time for search results to load

# Get results
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0, "No products found for the search query."

# Extract product names and click "Add to Cart"
for result in results:
    product_name = result.find_element(By.XPATH, ".//h4").text
    actualList.append(product_name)
    result.find_element(By.XPATH, ".//div/button").click()

# Debugging print statements
print("Expected List:", expectedList)
print("Actual List:", actualList)

# Validate the extracted list
assert expectedList == actualList, "Mismatch between expected and actual product list."

# Proceed to checkout
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Close the browser
time.sleep(5)
driver.quit()
