from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# defining the url to load and search the istqb key word
url = "https://www.google.com"
search_term = "istqb"

#fire up the browser and connect to eh url above
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

try:
    #Handle popup by clicking "Accept All" if it appears
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='L2AGLb']/div"))
    )
    accept_button.click()

    # Wait for the search bar to be visible and locate the search bar
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )

    search_bar.clear()
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)  # Submit the search form

    # Wait for search results to appear and click the first suggestion
    first_non_sponsored_suggestion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//h3[not(ancestor::*[@data-text-ad='1'])])[1]"))
    )
    first_non_sponsored_suggestion.click()
    time.sleep(3)

    print("Test Passed: New page opened for the search term.")
except Exception as e:
    print("Test Failed:", e)
finally:
    time.sleep(30)
    driver.quit()
