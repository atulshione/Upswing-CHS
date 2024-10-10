# import unittest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_setup import get_driver
# import random
# import string

# class TestSignUp(unittest.TestCase):

#     def setUp(self):
#         self.driver = get_driver()
#         self.driver.get("https://www.demoblaze.com/")
#         self.wait = WebDriverWait(self.driver, 30)  # Set up WebDriverWait
    
#     def tearDown(self):
#         self.driver.quit()

#     def generate_unique_username(self):
#         """Generate a unique username using a random string."""
#         return "user" + ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "@example.com"

#     def test_signup_positive(self):
#         driver = self.driver
#         wait = self.wait

#         username = self.generate_unique_username()
#         password = "newPassword1234"

#         # Open the Sign-up modal
#         wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()

#         # Wait for modal to fully load
#         wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='signInModal' and contains(@style, 'display: block')]")))

#         # Input valid credentials
#         username_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
#         password_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))

#         username_field.send_keys(username)
#         password_field.send_keys(password)

#         # Click the 'Sign up' button
#         signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))
#         signup_button.click()

#         # Handle success or error scenarios
#         try:
#             alert = wait.until(EC.alert_is_present())
#             alert_text = alert.text
#             print(f"Alert text: {alert_text}")  # Debugging line
#             if "Sign up successful." in alert_text:
#                 self.assertEqual(alert_text, "Sign up successful.", "Sign-up was not successful.")
#             elif "This user already exist." in alert_text:
#                 self.fail("Sign-up failed because user already exists. Consider using a unique username.")
#             elif "Please fill out Username and Password." in alert_text:
#                 self.fail("Sign-up failed due to empty fields. This should not happen with valid inputs.")
#             else:
#                 self.fail(f"Unexpected alert message: {alert_text}")
#             alert.accept()
#         except Exception as e:
#             self.fail(f"Sign-up process failed with exception: {e}")

#     def test_signup_negative(self):
#         driver = self.driver
#         wait = self.wait

#         # Open the Sign-up modal
#         wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()

#         # Wait for modal to fully load
#         wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='signInModal' and contains(@style, 'display: block')]")))

#         # Input invalid credentials (empty fields)
#         username_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
#         password_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))

#         username_field.send_keys("")  # Empty username
#         password_field.send_keys("")  # Empty password

#         # Click the 'Sign up' button
#         signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))
#         signup_button.click()

#         # Handle failure via alert
#         try:
#             alert = wait.until(EC.alert_is_present())
#             alert_text = alert.text
#             print(f"Alert text: {alert_text}")  # Debugging line
#             self.assertEqual(alert_text, "Please fill out Username and Password.", "Unexpected error message for invalid sign-up.")
#             alert.accept()
#         except Exception as e:
#             self.fail(f"Sign-up process failed with exception: {e}")

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_setup import get_driver
# from time import sleep
# from faker import Faker  # Import Faker
# import random

# class TestSignUp(unittest.TestCase):

#     def setUp(self):
#         self.driver = get_driver()
#         self.driver.get("https://www.demoblaze.com/")
#         self.wait = WebDriverWait(self.driver, 30)  # Set up WebDriverWait
#         self.faker = Faker()  # Initialize Faker
#         self.username = self.generate_unique_username()  # Global username
#         self.password = self.faker.password()  # Global password

#     def tearDown(self):
#         self.driver.quit()

#     def generate_unique_username(self):
#         """Generate a realistic unique username using Faker."""
#         return self.faker.user_name() + ''.join(random.choices("1234567890", k=4))  # Adds some randomness

#     def sign_up(self, username, password):
#         """Perform the sign-up process."""
#         wait = self.wait

#         # Open the Sign-up modal
#         wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()

#         # Wait for modal to fully load
#         wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='signInModal' and contains(@style, 'display: block')]")))
#         sleep(1)  # Adding sleep to ensure the modal is fully loaded

#         # Input credentials
#         username_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
#         password_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))

#         username_field.send_keys(username)
#         password_field.send_keys(password)

#         # Adding sleep to simulate a human action delay
#         sleep(1)

#         # Click the 'Sign up' button
#         signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))
#         signup_button.click()

#         # Adding sleep to ensure the alert can be triggered
#         sleep(2)

#     def test_signup_positive(self):
#         """Test case for valid sign up."""
#         print(f"Testing valid sign up with username: {self.username} and password: {self.password}")
#         self.sign_up(self.username, self.password)

#         # Handle success scenario
#         try:
#             alert = self.wait.until(EC.alert_is_present())
#             alert_text = alert.text
#             print(f"Alert text: {alert_text}")  # Debugging line
#             self.assertEqual(alert_text, "Sign up successful.", "Sign-up was not successful.")
#             alert.accept()  # Click OK on the alert
#             sleep(1)  # Ensure alert disappears before proceeding
#         except Exception as e:
#             self.fail(f"Sign-up process failed with exception: {e}")

#     def test_signup_with_used_username(self):
#         """Test case for signing up with an already used username."""
#         print(f"Testing sign up with used username: {self.username}")

#         # Now attempt to sign up again with the same username
#         self.sign_up("melissalong1500", self.faker.password())  # Use a different password

#         # Handle used username alert scenario
#         try:
#             alert = self.wait.until(EC.alert_is_present())
#             alert_text = alert.text
#             print(f"Alert text: {alert_text}")  # Debugging line
#             self.assertEqual(alert_text, "This user already exist.", "Unexpected alert for existing username.")
#             alert.accept()  # Click OK on the alert
#         except Exception as e:
#             self.fail(f"Sign-up process failed with exception: {e}")

#     def test_signup_with_empty_fields(self):
#         """Test case for signing up with empty fields."""
#         print("Testing sign up with empty fields")
#         self.sign_up("", "")  # Attempt to sign up with empty username and password

#         # Handle empty fields alert scenario
#         try:
#             alert = self.wait.until(EC.alert_is_present())
#             alert_text = alert.text
#             print(f"Alert text: {alert_text}")  # Debugging line
#             self.assertEqual(alert_text, "Please fill out Username and Password.", "Unexpected alert for empty fields.")
#             alert.accept()  # Click OK on the alert
#         except Exception as e:
#             self.fail(f"Sign-up process failed with exception: {e}")

# if __name__ == "__main__":
#     unittest.main()

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import get_driver
from time import sleep
from test_data import username, password  # Import the username and password

class TestSignUp(unittest.TestCase):

    def setUp(self):
        """Set up the WebDriver and navigate to the demo site."""
        self.driver = get_driver()
        self.driver.get("https://www.demoblaze.com/")
        self.wait = WebDriverWait(self.driver, 30)

    def tearDown(self):
        """Quit the WebDriver."""
        self.driver.quit()

    def sign_up(self, username, password):
        """Perform the sign-up process."""
        wait = self.wait

        # Open the Sign-up modal
        wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()

        # Wait for modal to fully load
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='signInModal' and contains(@style, 'display: block')]")))
        sleep(1)  # Adding sleep to ensure the modal is fully loaded

        # Input credentials
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "sign-password")))

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click the 'Sign up' button
        signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))
        signup_button.click()

        # Adding sleep to ensure the alert can be triggered
        sleep(2)

    def test_signup_positive(self):
        """Test case for valid sign up."""
        print(f"Testing valid sign up with username: {username} and password: {password}")
        self.sign_up(username, password)

        # Handle success scenario
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")  # Debugging line
            self.assertEqual(alert_text, "Sign up successful.", "Sign-up was not successful.")
            alert.accept()  # Click OK on the alert
            sleep(1)  # Ensure alert disappears before proceeding
        except Exception as e:
            self.fail(f"Sign-up process failed with exception: {e}")

    def test_signup_with_used_username(self):
        """Test case for signing up with an already used username."""
        print(f"Testing sign up with used username: {username}")

        # Attempt to sign up again with the same username
        self.sign_up(username, password)  # Use the same username

        # Handle used username alert scenario
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")  # Debugging line
            self.assertEqual(alert_text, "This user already exist.", "Unexpected alert for existing username.")
            alert.accept()  # Click OK on the alert
        except Exception as e:
            self.fail(f"Sign-up process failed with exception: {e}")

    def test_signup_with_empty_fields(self):
        """Test case for signing up with empty fields."""
        print("Testing sign up with empty fields")
        self.sign_up("", "")  # Attempt to sign up with empty username and password

        # Handle empty fields alert scenario
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")  # Debugging line
            self.assertEqual(alert_text, "Please fill out Username and Password.", "Unexpected alert for empty fields.")
            alert.accept()  # Click OK on the alert
        except Exception as e:
            self.fail(f"Sign-up process failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()


