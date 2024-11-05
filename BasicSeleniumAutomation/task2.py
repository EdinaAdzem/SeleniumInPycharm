from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()

#get to google
driver.get("https://www.google.com")
time.sleep(2)

#find and search
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("cats")
search_bar.send_keys(Keys.RETURN)

# add a delay and print title
time.sleep(3)
print("Page title:", driver.title)


driver.quit()
