from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#load page test
def test_page_load(setup_browser):
    driver = setup_browser
    driver.get('https://www.grocerymate.com')
    time.sleep(3)
    assert "GroceryMate" in driver.title
    print("Page loaded successfully!")

# login button available
def test_login_button(setup_browser):
    driver = setup_browser
    driver.get('https://www.grocerymate.com')
    time.sleep(3)

    try:
        login_button = driver.find_element(By.ID, 'login_button')
        assert login_button.is_displayed()
        print("Login button found and visible!")
    except Exception as e:
        pytest.fail(f"Login button not found: {str(e)}")

#login successfull



#products loaded test


#log out sucessful

