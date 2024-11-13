from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options to ignore SSL certificate errors
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--start-maximized")

# Set up the web driver
driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(30)

# Task 2 - Steps with XPath for grocerymate
# Step 1: Go to https://grocerymate.masterschool.com
driver.get("https://grocerymate.masterschool.com")

# Wait for 2 seconds for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']")))

# XPath for the icon/button you want to click
xpath = "//*[@id='root']/div/div[1]/div[2]/div[2]/div[1]/svg"

# Wait for the element to be clickable and then click it
try:
    login_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", login_icon)
    login_icon.click()
    print("Login icon clicked!")
except Exception as e:
    print("Error:", e)

# Step 2: Go to https://grocerymate.masterschool.com/auth
driver.get("https://grocerymate.masterschool.com/auth")

# Locate the input fields and buttons by xpath
email_xpath = "//*[@id='root']/div/div/div[1]/div[1]/div/form/input[1]"
password_xpath = "//*[@id='root']/div/div/div[1]/div[1]/div/form/input[2]"
sign_in_button_xpath = "//*[@id='root']/div/div/div[1]/div[1]/div/form/button"
create_account_link_xpath = "//*[@id='root']/div/div/div[1]/div[1]/div/form/a[1]"
go_to_home_link_xpath = "//*[@id='root']/div/div/div[1]/div[1]/div/form/a[2]"
email_input = driver.find_element(By.XPATH, email_xpath)
password_input = driver.find_element(By.XPATH, password_xpath)
sign_in_button = driver.find_element(By.XPATH, sign_in_button_xpath)
create_account_link = driver.find_element(By.XPATH, create_account_link_xpath)
go_to_home_link = driver.find_element(By.XPATH, go_to_home_link_xpath)

print("Email Input:", email_input)
print("Password Input:", password_input)
print("Sign In Button:", sign_in_button)
print("Create Account Link:", create_account_link)
print("Go to Home Link:", go_to_home_link)

# Step 3: Click on "Create a new account".
create_account_link.click()
full_name_xpath = "///*[@id='root']/div/div/div[1]/div[1]/div/form/input[1]"
email_signup_xpath = "//*[@id='root']/div/div/div[1]/div[1]/div/form/input[2]"
password_signup_xpath = "//*[@id='root']/div/div/div[1]/div[1]/div/form/input[3]"
sign_up_button_xpath = "//*[@id='root']/div/div/div[1]/div[1]/div/form/button"
full_name_input = driver.find_element(By.XPATH, full_name_xpath)
email_signup_input = driver.find_element(By.XPATH, email_signup_xpath)
password_signup_input = driver.find_element(By.XPATH, password_signup_xpath)
sign_up_button = driver.find_element(By.XPATH, sign_up_button_xpath)

print("Full Name Input:", full_name_input)
print("Email Signup Input:", email_signup_input)
print("Password Signup Input:", password_signup_input)
print("Sign Up Button:", sign_up_button)

# Step 4: Go to https://grocerymate.masterschool.com/store
driver.get("https://grocerymate.masterschool.com/store")

confirm_button_xpath = "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div/button"
confirm_button = driver.find_element(By.XPATH, confirm_button_xpath)
print("Confirm Button:", confirm_button)

# Step 5: Shop page, locate elements for Oranges
driver.get("https://grocerymate.masterschool.com/shop")
orange_quantity_xpath = "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/input"
orange_add_to_cart_xpath = "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/button"
orange_add_to_wishlist_xpath = "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div[3]/button]"
orange_quantity_input = driver.find_element(By.XPATH, orange_quantity_xpath)
orange_add_to_cart_button = driver.find_element(By.XPATH, orange_add_to_cart_xpath)
orange_add_to_wishlist_button = driver.find_element(By.XPATH, orange_add_to_wishlist_xpath)
print("Orange  Input scroll thingy:", orange_quantity_input)
print("Add to Cart Oranges:", orange_add_to_cart_button)
print("Add to Wishlist Oranges:", orange_add_to_wishlist_button)

# Close the browser
driver.quit()
