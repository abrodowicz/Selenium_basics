from selenium.webdriver.common.by import By
import random
import string
from pages.base_page import BasePage


class AuthenticationPage(BasePage):

    __AUTHENTICATION_EMAIL_CREATE_FIELD = (By.ID, 'email_create')
    __CREATE_ACCOUNT_SUBMIT_BUTTON = (By.XPATH, '//*[@id="SubmitCreate"]')
    __AUTHENTICATION_PAGE_TITLE = (By.XPATH, '//*[@id="columns"]/div[1]/span[2][text()="	Authentication"]')

    def random_mail(self, char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

    def sign_in_to_application(self):
        self.fill(by_locator=self.__AUTHENTICATION_EMAIL_CREATE_FIELD, value=self.random_mail(7) + "@gmail.com")
        self.click(by_locator=self.__CREATE_ACCOUNT_SUBMIT_BUTTON)

    def authentication_page_title(self):
        return self.get_element(by_locator=self.__AUTHENTICATION_PAGE_TITLE)
