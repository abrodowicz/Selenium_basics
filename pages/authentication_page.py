from selenium.webdriver.common.by import By
import random
import string

class AuthenticationPage:

    def random_char(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(self))

    def _init_(self, driver):
        self.driver = driver

    def sign_in_to_application(self):
        self.driver.find_element(By.ID, 'email_create').send_keys(random_char(7) + "@gmail.com")
        self.driver.find_element(By.XPATH, '//*[@id="SubmitCreate"]').click()
