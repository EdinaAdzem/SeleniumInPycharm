"""Linkedin login process automated."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#LinkedIn credentials
linkedin_email = "edina.plakalo@gmail.com"
linkedin_password = "Piramida2026!@"


driver = webdriver.Chrome()
driver.maximize_window()

#LinkedIn login page
driver.get("https://www.linkedin.com/login")
time.sleep(2)

#locate the fields and enter creds
email_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

email_field.send_keys(linkedin_email)
password_field.send_keys(linkedin_password)

#submit login
password_field.send_keys(Keys.RETURN)


time.sleep(3)
print("Logged in page title:", driver.title)


driver.quit()
