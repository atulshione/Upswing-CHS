import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import get_driver
from test_data import username, password

class TestLogout(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.get("https://www.demoblaze.com/")
    
    def tearDown(self):
        self.driver.quit()

    def test_logout_positive(self):
        driver = self.driver
        wait = self.wait

        # Perform login
        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

        driver.find_element(By.ID, "loginusername").send_keys(username) 
        driver.find_element(By.ID, "loginpassword").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()

        # Wait for login to complete
        wait.until(EC.visibility_of_element_located((By.ID, "logout2")))

        # Perform logout
        wait.until(EC.element_to_be_clickable((By.ID, "logout2"))).click()

        # Verify successful logout
        try:
            # After logout, the login button should be visible
            wait.until(EC.element_to_be_clickable((By.ID, "login2")))
            self.assertTrue(driver.find_element(By.ID, "login2").is_displayed(), "Logout was not successful.")
        except Exception as e:
            self.fail(f"Logout positive test failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
