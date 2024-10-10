import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import get_driver
from test_data import full_name, credit_card_number, country, city, rndint, month, year
import time  # Import time for sleep functionality

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://www.demoblaze.com/")
        self.wait = WebDriverWait(self.driver, 60)

    def tearDown(self):
        self.driver.quit()

    def add_product_to_cart(self, category, product_name):
        driver = self.driver
        wait = self.wait

        # wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home"))).click()
        # print("Clicked on Home link.")

        # Navigate to the specified category
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category))).click()
        print(f"Selected category: {category}")

        # Click on the specified product
        product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, product_name)))
        product.click()
        print(f"Viewing product details for: {product_name}")

        # Add the product to the cart
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-success.btn-lg"))).click()
        print(f"Clicked 'Add to Cart' for {product_name}")

        # Handle the alert for product added to cart
        try:
            alert = wait.until(EC.alert_is_present())
            alert.accept()  # Accept the alert
            print(f"Product '{product_name}' added to cart successfully.")
        except Exception as e:
            self.fail(f"Unexpected alert present: {e}")

    def wait_for_purchase_and_click(self):
        try:
            purchase_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='purchaseOrder()']")))
            print("Purchase button is visible and clickable.")
            purchase_button.click()
            print("Clicked on Purchase button.")
        except Exception as e:
            self.fail(f"Purchase button not found or not clickable: {e}")

    def fill_checkout_form(self, name=full_name, country=country, city=city, card=credit_card_number, month=month, year=year):
        wait = self.wait
        wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(name)
        wait.until(EC.element_to_be_clickable((By.ID, "country"))).send_keys(country)
        wait.until(EC.element_to_be_clickable((By.ID, "city"))).send_keys(city)
        wait.until(EC.element_to_be_clickable((By.ID, "card"))).send_keys(card)
        wait.until(EC.element_to_be_clickable((By.ID, "month"))).send_keys(month)
        wait.until(EC.element_to_be_clickable((By.ID, "year"))).send_keys(year)

    def verify_order_success(self):
        try:
            success_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sweet-alert"))).text
            self.assertIn("Thank you for your purchase!", success_message)
            print("Order placed successfully.")
            print(f"Order details: {success_message}")
        except Exception as e:
            self.fail(f"Confirmation message not found: {e}")

    def checkout_with_incomplete_info(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the cart
        wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()


        # Fill out the checkout form with incomplete information
        self.fill_checkout_form()

        # Wait for the purchase button and click it
        self.wait_for_purchase_and_click()

        # Verify the confirmation message
        self.verify_order_success()

    def test_checkout_with_items(self):

        """Test the checkout process with items in the cart."""
        driver = self.driver
        wait = self.wait
        # Step 1: Add Samsung Galaxy S6
        self.add_product_to_cart("Phones", "Samsung galaxy s6")
        wait = WebDriverWait(driver,15)

        driver.find_element(By.ID, 'nava').click()

        # Step 2: Add MacBook Pro
        self.add_product_to_cart("Laptops", "MacBook Pro")
        wait = WebDriverWait(driver,15)

        driver.find_element(By.ID, 'nava').click()

        # Step 3: Add ASUS Full HD
        self.add_product_to_cart("Monitors", "ASUS Full HD")
        wait = WebDriverWait(driver,15)

        # Navigate to the cart
        wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success"))).click()

        self.fill_checkout_form()
        self.wait_for_purchase_and_click()

        # Verify the confirmation message
        self.verify_order_success()


    def test_checkout_with_empty_cart(self):
        """Test the checkout process with an empty cart."""
        driver = self.driver
        wait = self.wait

        # Navigate to the cart
        wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()

        # Check if the cart is empty
        cart_table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table")))
        cart_rows = cart_table.find_elements(By.CSS_SELECTOR, "tbody tr")

        if len(cart_rows) == 0:
            print("Cart is empty. Proceeding with checkout.")
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success"))).click()

            # Fill out the checkout form with incomplete information
            self.fill_checkout_form()

            # Wait for the purchase button and click it
            self.wait_for_purchase_and_click()

            # Verify the confirmation message
            self.verify_order_success()
        else:
            self.fail("Cart is not empty, which is not expected for this test.")

if __name__ == "__main__":
    unittest.main()
