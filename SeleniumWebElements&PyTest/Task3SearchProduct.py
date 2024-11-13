from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://automationexercise.com")
assert "Automation Exercise" in driver.title

products_button = driver.find_element(By.LINK_TEXT, "Products")
products_button.click()

time.sleep(2)
assert "All Products" in driver.page_source

search_input = driver.find_element(By.ID, "search_product")
search_input.send_keys("furniture")
search_input.send_keys(Keys.RETURN)

time.sleep(2)
assert "Searched Products" in driver.page_source

product_list = driver.find_elements(By.CLASS_NAME, "some productinfo")
assert len(product_list) > 0

driver.quit()
