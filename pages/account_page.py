from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):

    __ACCOUNT_PAGE_TITLE = (By.XPATH, '//*[@id="columns"]/div[1]/span[2][text()="My account"]')

    def account_page_title(self):
        self.if_element_present(by_locator=self.__ACCOUNT_PAGE_TITLE)
