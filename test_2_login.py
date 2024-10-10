# import unittest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_setup import get_driver

# class TestLogin(unittest.TestCase):

#     def setUp(self):
#         self.driver = get_driver()
#         self.wait = WebDriverWait(self.driver, 20)
#         self.driver.get("https://www.demoblaze.com/")
    
#     def tearDown(self):
#         self.driver.quit()

#     def test_login_positive(self):
#         driver = self.driver
#         wait = self.wait

#         # Perform login with valid credentials
#         wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
#         wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

#         driver.find_element(By.ID, "loginusername").send_keys("yk@gmail.com")
#         driver.find_element(By.ID, "loginpassword").send_keys("Yk@123")
#         driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

#         # Validate successful login
#         try:
#             # Check if the logout button is visible to confirm successful login
#             wait.until(EC.visibility_of_element_located((By.ID, "logout2")))
#             self.assertTrue(driver.find_element(By.ID, "logout2").is_displayed(), "Login was not successful.")
            
#             # Log out after successful login
#             driver.find_element(By.ID, "logout2").click()
            
#             # Confirm logout by checking that login button is visible again
#             wait.until(EC.visibility_of_element_located((By.ID, "login2")))
#             self.assertTrue(driver.find_element(By.ID, "login2").is_displayed(), "Logout was not successful.")
#         except Exception as e:
#             self.fail(f"Login positive test failed with exception: {e}")

#     def test_login_negative(self):
#         driver = self.driver
#         wait = self.wait

#         # Perform login with invalid credentials
#         wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
#         wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

#         driver.find_element(By.ID, "loginusername").send_keys("invalid_user")
#         driver.find_element(By.ID, "loginpassword").send_keys("wrong_password")
#         driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

#         # Validate failure
#         try:
#             alert = wait.until(EC.alert_is_present())
#             self.assertEqual(alert.text, "Wrong password.", "Alert text did not match the expected 'Wrong password.'")
#             alert.accept()
#         except Exception as e:
#             self.fail(f"Login negative test failed with exception: {e}")

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_setup import get_driver
# from test_data import username, password  # Import the username and password

# class TestLogin(unittest.TestCase):

#     def setUp(self):
#         self.driver = get_driver()
#         self.wait = WebDriverWait(self.driver, 20)
#         self.driver.get("https://www.demoblaze.com/")

#     def tearDown(self):
#         self.driver.quit()

#     def test_login_positive(self):
#         driver = self.driver
#         wait = self.wait

#         # Perform login with valid credentials from signup
#         wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
#         wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

#         driver.find_element(By.ID, "loginusername").send_keys(username)
#         driver.find_element(By.ID, "loginpassword").send_keys(password)
#         driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

#         # Validate successful login
#         try:
#             wait.until(EC.visibility_of_element_located((By.ID, "logout2")))
#             self.assertTrue(driver.find_element(By.ID, "logout2").is_displayed(), "Login was not successful.")
            
#             # Log out after successful login
#             driver.find_element(By.ID, "logout2").click()
#             wait.until(EC.visibility_of_element_located((By.ID, "login2")))
#             self.assertTrue(driver.find_element(By.ID, "login2").is_displayed(), "Logout was not successful.")
#         except Exception as e:
#             self.fail(f"Login positive test failed with exception: {e}")

#     def test_login_negative(self):
#         driver = self.driver
#         wait = self.wait

#         # Perform login with invalid credentials
#         wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
#         wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

#         driver.find_element(By.ID, "loginusername").send_keys("invalid_user")
#         driver.find_element(By.ID, "loginpassword").send_keys("wrong_password")
#         driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

#         # Validate failure
#         try:
#             alert = wait.until(EC.alert_is_present())
#             self.assertEqual(alert.text, "Wrong password.", "Alert text did not match the expected 'Wrong password.'")
#             alert.accept()
#         except Exception as e:
#             self.fail(f"Login negative test failed with exception: {e}")

# if __name__ == "__main__":
#     unittest.main()

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import get_driver
import time
from test_data import username, password  # Import the username and password

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("https://www.demoblaze.com/")

    def tearDown(self):
        self.driver.quit()

    def handle_alert(self):
        """Handles the alert and returns the alert text."""
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()  # Close the alert
            return alert_text
        except Exception as e:
            return None

    def test_login_empty_fields(self):
        """Test case for logging in with empty fields."""
        driver = self.driver

        # Click on the 'Log in' link
        self.wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))
        time.sleep(2)

        # Leave fields empty and click on the 'Log in' button
        driver.find_element(By.ID, "loginusername").send_keys("")
        driver.find_element(By.ID, "loginpassword").send_keys("")
        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
        time.sleep(2)

        # Validate alert for empty fields
        alert_text = self.handle_alert()
        self.assertEqual(alert_text, "Please fill out Username and Password.", "Alert text did not match the expected 'Please fill out Username and Password.'")

    def test_login_valid_username_invalid_password(self):
        """Test case for logging in with valid username and invalid password."""
        driver = self.driver

        # Click on the 'Log in' link
        self.wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

        # Enter a valid username and an invalid password
        driver.find_element(By.ID, "loginusername").send_keys(username)
        driver.find_element(By.ID, "loginpassword").send_keys("wrong_password")
        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

        # Validate alert for wrong password
        alert_text = self.handle_alert()
        self.assertEqual(alert_text, "Wrong password.", "Alert text did not match the expected 'Wrong password.'")

    def test_login_invalid_username(self):
        """Test case for logging in with invalid username."""
        driver = self.driver

        # Click on the 'Log in' link
        self.wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

        # Enter an invalid username and any password
        driver.find_element(By.ID, "loginusername").send_keys("invalid_user")
        driver.find_element(By.ID, "loginpassword").send_keys("any_password")
        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

        # Validate alert for user does not exist
        alert_text = self.handle_alert()
        self.assertEqual(alert_text, "Wrong password.", "Alert text did not match the expected 'User does not exist.'")

    def test_login_valid_user(self):
        """Test case for valid login."""
        driver = self.driver

        # Click on the 'Log in' link
        self.wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

        # Enter valid credentials
        driver.find_element(By.ID, "loginusername").send_keys(username)
        driver.find_element(By.ID, "loginpassword").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

        # Wait for the login to complete and check if the welcome message is displayed
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f'//a[contains(text(), "Welcome {username}")]')))
        
        logincheck = driver.find_element(By.XPATH, f'//a[contains(text(), "Welcome {username}")]').is_displayed()
        print(f'Login is successful. Username displayed: {logincheck}')
        
        # Assert that the welcome message is displayed
        self.assertTrue(logincheck, f'Expected welcome message for {username} to be displayed.')

        # Optionally log out
        driver.find_element(By.ID, "logout2").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login2")))
        self.assertTrue(driver.find_element(By.ID, "login2").is_displayed(), "Logout was not successful.")

if __name__ == "__main__":
    unittest.main()


