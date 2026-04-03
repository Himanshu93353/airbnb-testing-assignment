04.04 2:01 AM
test_airbnb.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Base URL
base_url = "https://example-airbnb-clone.com"

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Wait object
wait = WebDriverWait(driver, 10)

try:
    # LOGIN TEST
    driver.get(f"{base_url}/login")

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    email_input.send_keys("test@mail.com")

    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login").click()

    wait.until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()

    print("Login Test Passed")

    # BOOKING FLOW
    driver.get(f"{base_url}/search")

    location_input = wait.until(EC.visibility_of_element_located((By.ID, "location")))
    location_input.send_keys("Goa")
    location_input.send_keys(Keys.ENTER)

    property_card = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".property-card"))
    )
    property_card.click()

    reserve_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "reserve"))
    )
    reserve_btn.click()

    confirmation = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "booking-confirmation"))
    )

    assert "confirmed" in confirmation.text.lower()

    print("Booking Test Passed")

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()
