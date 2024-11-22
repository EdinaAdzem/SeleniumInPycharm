from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1.load the URL
url = 'http://automationexercise.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

try:
    # Handle consent popup if it appears
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Consent')]"))
    ).click()

    # Wait for the overlay to disappear (if it appears)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "fc-dialog-overlay"))
    )

    # find and click the login and sign button best located with xpath
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/login' and contains(., 'Signup / Login')]"))
    )

    driver.execute_script("arguments[0].click();", login_button)


    # 5 check if the 'New User Signup!' is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'New User Signup!')]"))
    )
    print("New User Signup! is visible")

    # 6. Enter name and email address using the provided XPaths
    name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]'))
    )
    name_field.send_keys('Collamity Jane')
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

    # fill in the account form
    title_radio_button = driver.find_element(By.ID, "uniform-id_gender1")
    title_radio_button.click()

    name_field = driver.find_element(By.ID, "customer_firstname")
    name_field.send_keys("Calamity")
    last_name_field = driver.find_element(By.ID, "customer_lastname")
    last_name_field.send_keys("Jane")
    password_field = driver.find_element(By.ID, "passwd")
    password_field.send_keys("password123Jane")
    dob_day = driver.find_element(By.ID, "days")  # Optimized to use ID
    dob_day.click()
    # 10. Select checkbox 'Sign up for our newsletter!'
    newsletter_checkbox = driver.find_element(By.ID, "newsletter")  # Optimized to use ID
    newsletter_checkbox.click()

    # 11. Select checkbox 'Receive special offers from our partners!'
    offers_checkbox = driver.find_element(By.ID, "optin")  # Optimized to use ID
    offers_checkbox.click()

    # 12. Fill details: Address, Country, State, City, Zipcode, Mobile Number
    address1_field = driver.find_element(By.ID, "address1")  # Optimized to use ID
    address1_field.send_keys("123 Wild West St.")

    address2_field = driver.find_element(By.ID, "address2")  # Optimized to use ID
    address2_field.send_keys("Apt 5A")

    # Country Dropdown (Using ID for optimization)
    country_dropdown = driver.find_element(By.ID, "id_country")
    country_dropdown.click()

    # State (If using dropdown, you can select a value here or type it)
    state_field = driver.find_element(By.ID, "id_state")
    state_field.send_keys("Arizona")

    # City field
    city_field = driver.find_element(By.ID, "city")
    city_field.send_keys("Dublin")

    # Zipcode
    zipcode_field = driver.find_element(By.ID, "zipcode")
    zipcode_field.send_keys("72160")

    # Mobile Number field
    mobile_number_field = driver.find_element(By.ID, "mobile_number")
    mobile_number_field.send_keys("1234567890")

    # 13. Click 'Create Account' button
    create_account_button = driver.find_element(By.ID, "submitAccount")
    create_account_button.click()

    # 14. check if  'ACCOUNT CREATED!' is visible
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
