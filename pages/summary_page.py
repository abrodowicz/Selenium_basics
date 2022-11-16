from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SummaryPage(BasePage):

    __SUMMARY_PAGE_TITLE = (By.XPATH, '//*[@id="columns"]/div[1]/span[2][text()="Your shopping cart"]')
    __TRASH_ICON = (By.XPATH, '//*[@id="5_19_0_0"]/i')
    __PRODUCT_QUANTITY = (By.XPATH, '//*[@id="summary_products_quantity"][text()="1 Product"]')

    def summary_page_title(self):
        self.if_element_present(by_locator=self.__SUMMARY_PAGE_TITLE)

    def click_trash_icon(self):
        self.click(by_locator=self.__TRASH_ICON)

    def summary_page_product_quantity(self):
        self.if_element_present(by_locator=self.__PRODUCT_QUANTITY)
