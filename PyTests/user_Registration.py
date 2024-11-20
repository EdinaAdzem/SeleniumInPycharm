from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_registration_success(driver):
    driver.get("https://automationexercise.com/login")

    # Click the Signup/Login button
    signup_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))
    )
    signup_button.click()

    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys("testuser123@example.com")
    driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("Password123")
    driver.find_element(By.NAME, "days").send_keys("1")
    driver.find_element(By.NAME, "months").send_keys("January")
    driver.find_element(By.NAME, "years").send_keys("2000")
    driver.find_element(By.XPATH, '//button[@data-qa="create-account"]').click()

    success_message = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//b[text()="Account Created!"]'))
    )
    assert success_message.is_displayed()


def test_user_registration_existing_user(driver):
    driver.get("https://automationexercise.com/login")

    # Try to register with an existing email
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys("existinguser@example.com")
    driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()


    error_message = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "Email Address already exist!")]'))
    )
    assert error_message.is_displayed()
