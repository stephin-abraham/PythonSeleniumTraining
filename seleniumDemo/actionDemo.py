import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()
word = driver.find_element(By.XPATH,"//a[text()='Top']").text
print(word)
action.context_click(driver.find_element(By.LINK_TEXT,'Top')).perform()
word2 = driver.find_element(By.XPATH,"//a[text()='Reload']").text
print(word2)
action.move_to_element(driver.find_element(By.LINK_TEXT,'Reload')).click().perform()