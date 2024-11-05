from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Set up chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the local sample.html file
file_path = os.path.abspath("sample.html")
driver.get(f"file:///{file_path}")


time.sleep(2)

#find the input field by its ID and enter text
input_field = driver.find_element(By.ID, "inputField")
input_field.send_keys("Hello, Selenium!")

#a delay, then locate and click the submit button
time.sleep(2)
submit_button = driver.find_element(By.ID, "submitButton")
submit_button.click()

#Final delay and quit the browser
time.sleep(2)
driver.quit()
