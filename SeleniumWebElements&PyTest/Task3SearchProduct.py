from selenium import webdriver
from selenium.common import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://automationexercise.com"
search_item = "shirt"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

assert "Automation Exercise" in driver.title

try:
    # Handle consent popup if it appears
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Consent')]"))
    ).click()

    # Wait for the overlay to disappear (if it appears)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "fc-dialog-overlay"))
    )

    # find and click the products button best located with xpath
    products_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/products"]'))
    )
    driver.execute_script("arguments[0].click();", products_button)

    #wait for all prods
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "All Products")
    )
except Exception as e:
    print(f"Error while clicking Products button: {e}")
    driver.quit()


try:
    # Handle overlay OR some interceptors
    print("Checking for overlay...")
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element((By.CLASS_NAME, "fc-dialog-overlay"))
    )
    print("Overlay dismissed or not present.")

    # Locate and interact with the search input
    print("Waiting for the search input field...")
    search_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='search_product']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", search_input)
    search_input.click()
    search_input.clear()
    search_input.send_keys("shirt")

    #submit button
    print("Waiting for the submit button...")
    submit_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='submit_search']"))
    )
    submit_button.click()

    # Wait for search
    print("Waiting for search results...")
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Searched Products")
    )
    print("Search completed successfully!")
except Exception as e:
    print("An error occurred:", e)

try:
    # Verify search results
    product_list = driver.find_elements(By.CLASS_NAME, "productinfo")
    assert len(product_list) > 0
except Exception as e:
    print(f"Error while verifying search results: {e}")
    driver.quit()


print("Home Page is visible")

driver.quit()
