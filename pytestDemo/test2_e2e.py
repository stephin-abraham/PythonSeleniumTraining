from selenium.webdriver.common.by import By


def test_e2e(browserInstance):
    driver= browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID, "username").send_keys("rahulshettayacademy")
    driver.find_element(By.NAME,"password").send_keys("Learning")
    driver.find_element(By.ID,"signInBtn").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='shop']").click()
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for product in products:
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()