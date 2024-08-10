from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  
driver.get("https://example-ecommerce.com")  

def add_item_to_cart(item_id):
    try:
        item = driver.find_element(By.ID, item_id)
        item.click()
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
        add_to_cart_button.click()
    except NoSuchElementException:
        print(f"Item {item_id} not found or not available.")

def proceed_to_checkout():
    try:
        checkout_button = driver.find_element(By.ID, "proceed-to-checkout")
        checkout_button.click()
    except NoSuchElementException:
        print("Checkout button not found.")

def enter_payment_details(card_number, expiry_date, cvv):
    try:
        card_number_field = driver.find_element(By.ID, "card-number")
        expiry_date_field = driver.find_element(By.ID, "expiry-date")
        cvv_field = driver.find_element(By.ID, "cvv")

        card_number_field.send_keys(card_number)
        expiry_date_field.send_keys(expiry_date)
        cvv_field.send_keys(cvv)
    except NoSuchElementException:
        print("Payment fields not found.")

def verify_cart_total(expected_total):
    try:
        cart_total = driver.find_element(By.ID, "cart-total").text
        assert cart_total == expected_total, f"Expected {expected_total}, but got {cart_total}"
        print("Cart total is correct.")
    except NoSuchElementException:
        print("Cart total not found.")
    except AssertionError as e:
        print(e)

def test_add_single_item_to_cart_and_checkout():
    add_item_to_cart("item-1")
    proceed_to_checkout()

def test_add_multiple_items_to_cart_and_checkout():
    add_item_to_cart("item-1")
    add_item_to_cart("item-2")
    proceed_to_checkout()

def test_verify_cart_total():
    add_item_to_cart("item-1")
    verify_cart_total("$100.00")  # Replace with the actual expected total

def test_proceed_to_checkout_with_invalid_payment_details():
    proceed_to_checkout()
    enter_payment_details("1234567890123456", "12/23", "123")  # Invalid card details
    # Verify error message
    try:
        error_message = driver.find_element(By.ID, "payment-error").text
        assert error_message == "Invalid payment details", f"Expected error message not found: {error_message}"
        print("Invalid payment details test passed.")
    except NoSuchElementException:
        print("Error message not found.")
    except AssertionError as e:
        print(e)

def test_proceed_to_checkout_with_empty_cart():
    proceed_to_checkout()
    try:
        error_message = driver.find_element(By.ID, "cart-error").text
        assert error_message == "Your cart is empty.", f"Expected error message not found: {error_message}"
        print("Empty cart checkout test passed.")
    except NoSuchElementException:
        print("Error message not found.")
    except AssertionError as e:
        print(e)

def test_add_out_of_stock_item_to_cart():
    add_item_to_cart("out-of-stock-item")
    try:
        error_message = driver.find_element(By.ID, "stock-error").text
        assert error_message == "Item is out of stock", f"Expected error message not found: {error_message}"
        print("Out of stock item test passed.")
    except NoSuchElementException:
        print("Error message not found.")
    except AssertionError as e:
        print(e)

# Run Test Cases
test_add_single_item_to_cart_and_checkout()
test_add_multiple_items_to_cart_and_checkout()
test_verify_cart_total()
test_proceed_to_checkout_with_invalid_payment_details()
test_proceed_to_checkout_with_empty_cart()
test_add_out_of_stock_item_to_cart()

# Close the browser session
driver.quit()
