from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_search_valid(driver):
    driver.get("https://automationexercise.com/products")

    # Search for a valid product
    search_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "search_product"))
    )
    search_input.send_keys("shirt")
    driver.find_element(By.ID, "submit_search").click()

    # Verify search results
    results = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//h2[contains(text(), "Searched Products")]'))
    )
    assert results.is_displayed()


def test_product_search_invalid(driver):
    driver.get("https://automationexercise.com/products")

    #check invalid data
    search_input = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "search_product"))
    )
    search_input.send_keys("nonexistentproduct")
    driver.find_element(By.ID, "submit_search").click()

    # no prods have been founr
    no_results_message = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "No products found")]'))
    )
    assert no_results_message.is_displayed()
