import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import get_driver
from selenium.webdriver.support.ui import WebDriverWait

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://www.demoblaze.com/")
        self.wait = WebDriverWait(self.driver, 60)  # Set up WebDriverWait

    def tearDown(self):
        self.driver.quit()

    def navigate_to_last_page(self):
        driver = self.driver
        wait = self.wait
        
        # Wait until the product grid is loaded
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card")))

        # Navigate to the last page by repeatedly clicking "Next"
        while True:
            try:
                next_button = wait.until(EC.element_to_be_clickable((By.ID, "next2")))  # Update ID as needed
                next_button.click()
                
                # Wait for the products to load on the new page
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card")))
                
                # Small sleep to allow the page to load properly
                driver.implicitly_wait(1)  # Optional: could be removed
                
            except Exception as e:
                # If "Next" button is not clickable anymore, it means we're on the last page
                print("Reached the last page or encountered an issue with pagination.")
                break

    def add_last_product_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Select the last product on the last page
        products = driver.find_elements(By.CLASS_NAME, "card")
        if products:
            last_product = products[-1]
            wait = WebDriverWait(driver, 10)
            last_product_title = last_product.find_element(By.CLASS_NAME, "hrefch").text
            print(f"Adding product: {last_product_title} to cart")
            
            # Click the product to view details
            wait = WebDriverWait(driver, 10)
            last_product.find_element(By.CLASS_NAME, "hrefch").click()

            # Wait for the product page to load and add the product to cart
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-success.btn-lg"))).click()
            
            # Handle the alert for product added to cart
            try:
                alert = wait.until(EC.alert_is_present())
                alert.accept()  # Accept the alert
                print(f"Product '{last_product_title}' added to cart successfully.")
            except Exception as e:
                self.fail(f"Unexpected alert present: {e}")
        else:
            self.fail("No products found on the last page.")

    def test_add_last_product_to_cart(self):
        # Navigate to the last page
        self.navigate_to_last_page()

        # Add the last product on the last page to the cart
        self.add_last_product_to_cart()

if __name__ == "__main__":
    unittest.main()
