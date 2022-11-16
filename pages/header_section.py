from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HeaderSection(BasePage):

    __HEADER_SIGNIN_BUTTON = (By.XPATH, '//a[@title="Log in to your customer account"]')
    __HEADER_NICKNAME_TEXT = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span[text()="Tester Testowy"]')
    __HEADER_LOGOUT_BUTTON = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')

    def click_sign_in_button(self):
        self.click(by_locator=self.__HEADER_SIGNIN_BUTTON)

    def check_if_nickname_is_presented(self):
        self.if_element_present(by_locator=self.__HEADER_NICKNAME_TEXT)

    def click_logout_button(self):
        self.click(by_locator=self.__HEADER_LOGOUT_BUTTON)
