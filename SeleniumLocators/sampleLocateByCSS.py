from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Set up the web driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the local HTML file
file_path = os.path.abspath("sample.html")
driver.get(f"file:///{file_path}")

time.sleep(2)

#Locate the input field using CSS selector and enter the text
input_field = driver.find_element(By.CSS_SELECTOR, "#inputField")  # CSS input field
input_field.send_keys("Hello, Selenium with CSS!")

#locate and click the submit button using CSS selector
time.sleep(2)
submit_button = driver.find_element(By.CSS_SELECTOR, "#submitButton")  # CSS  for  button
submit_button.click()

#delay to observe output and quit the browser
time.sleep(2)
driver.quit()