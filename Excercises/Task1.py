from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the web driver for the browesr in use
driver = webdriver.Chrome()
driver.maximize_window()

# go to url
driver.get("https://masterschool.com")
time.sleep(2)  # Wait for 2-3 seconds for the page to load

#locate the link
try:
    browse_programs_link = driver.find_element(By.LINK_TEXT, "Browse Programs")
    time.sleep(2)  #wait here
    browse_programs_link.click()
    time.sleep(2)  #wait for after click
finally:
    #close the browser
    driver.quit()
