from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Launch browser and navigate to URL
url = 'http://automationexercise.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

try:
    # 2. Handle consent popup if it appears
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p"))
    ).click()

    # 3. Verify Home Page is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Full-Fledged practice website for Automation testing')]"))
    )
    print("Home Page is visible")

    # 4. Click on 'Signup / Login' button using the provided XPath for register button
    signup_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'))
    )
    signup_login_button.click()

    # 5. Verify 'New User Signup!' is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'New User Signup!')]"))
    )
    print("New User Signup! is visible")

    # 6. Enter name and email address using the provided XPaths
    # Enter the name in the name input field
    name_field = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
    name_field.send_keys('Collamity Jane')

    # Enter the email in the email input field
    email_field = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
    email_field.send_keys('collamity.jane@example.com')

    # 7. Click 'Signup' button
    signup_button = driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button")
    signup_button.click()

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Enter Account Information')]"))
    )
    print("ENTER ACCOUNT INFORMATION is visible")

    # 9. Fill details: Title, Name, Email, Password, Date of birth
    title_radio_button = driver.find_element(By.XPATH, "//*[@id='uniform-id_gender1']")
    title_radio_button.click()  # Select Mr.

    # Fill Name, Email, and Password
    name_field = driver.find_element(By.XPATH, "//*[@id='account_creation']/div[1]/div[1]/input")
    name_field.send_keys("Calamity Jane")  # Updated to Calamity Jane

    password_field = driver.find_element(By.XPATH, "//*[@id='account_creation']/div[1]/div[2]/input")
    password_field.send_keys("password123")

    # Select Date of Birth
    dob_day = driver.find_element(By.XPATH, "//*[@id='uniform-days']")
    dob_day.click()

    # 10. Select checkbox 'Sign up for our newsletter!'
    newsletter_checkbox = driver.find_element(By.XPATH, "//*[@id='uniform-newsletter']")
    newsletter_checkbox.click()

    # 11. Select checkbox 'Receive special offers from our partners!'
    offers_checkbox = driver.find_element(By.XPATH, "//*[@id='uniform-optin']")
    offers_checkbox.click()

    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    first_name_field = driver.find_element(By.XPATH, "//*[@id='customer_firstname']")
    first_name_field.send_keys("Calamity")

    last_name_field = driver.find_element(By.XPATH, "//*[@id='customer_lastname']")
    last_name_field.send_keys("Jane")

    company_field = driver.find_element(By.XPATH, "//*[@id='company']")
    company_field.send_keys("Wild West Inc.")

    address1_field = driver.find_element(By.XPATH, "//*[@id='address1']")
    address1_field.send_keys("123 Wild West St.")

    address2_field = driver.find_element(By.XPATH, "//*[@id='address2']")
    address2_field.send_keys("Apt 5A")

    country_dropdown = driver.find_element(By.XPATH, "//*[@id='uniform-id_country']")
    country_dropdown.click()

    state_field = driver.find_element(By.XPATH, "//*[@id='id_state']")
    state_field.send_keys("Arizona")

    city_field = driver.find_element(By.XPATH, "//*[@id='city']")
    city_field.send_keys("Tombstone")

    zipcode_field = driver.find_element(By.XPATH, "//*[@id='zipcode']")
    zipcode_field.send_keys("85638")

    mobile_number_field = driver.find_element(By.XPATH, "//*[@id='mobile_number']")
    mobile_number_field.send_keys("1234567890")

    # 13. Click 'Create Account' button
    create_account_button = driver.find_element(By.XPATH, "//*[@id='submitAccount']")
    create_account_button.click()

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Account Created!')]"))
    )
    print("ACCOUNT CREATED! is visible")

    # 15. Click 'Continue' button
    continue_button = driver.find_element(By.XPATH, "//a[@href='/']")
    continue_button.click()

    # 16. Verify that 'Logged in as username' is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//i[contains(text(),'Logged in as')]"))
    )
    print("Logged in as Calamity Jane is visible")

    # 17. Click 'Delete Account' button
    delete_account_button = driver.find_element(By.XPATH, "//a[@href='/delete_account']")
    delete_account_button.click()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Account Deleted!')]"))
    )
    print("ACCOUNT DELETED! is visible")

    continue_button = driver.find_element(By.XPATH, "//a[@href='/']")
    continue_button.click()

except Exception as e:
    print("Test Failed:", e)
finally:
    # Add a delay before quitting the browser to view the result
    time.sleep(5)
    driver.quit()
