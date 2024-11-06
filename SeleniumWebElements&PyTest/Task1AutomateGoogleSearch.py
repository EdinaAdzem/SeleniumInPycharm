from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.google.com"
search_term = "istqb"

# This will install the ChromeDriver and manage its version
driver = webdriver.Chrome(ChromeDriverManager().install())
print("ChromeDriver path:", ChromeDriverManager().install())

# Maximize the window for better visibility
driver.maximize_window()
driver.get(url)

try:
    # Wait for the search bar to be visible
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )

    search_bar.clear()
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)  # Submit the search form

    # Wait for search results to appear and click the first suggestion
    first_suggestion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h3[contains(text(), 'ISTQB')]"))
    )
    first_suggestion.click()

    # Wait until the new page is loaded and the title contains the search term
    WebDriverWait(driver, 10).until(
        EC.title_contains(search_term)
    )

    print("Test Passed: New page opened for the search term.")
except Exception as e:
    print("Test Failed:", e)
finally:
    driver.quit()
