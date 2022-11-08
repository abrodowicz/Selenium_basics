from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchSection(BasePage):

    __SEARCH_FIELD = (By.ID, "search_query_top")
    __SEARCH_BUTTON = (By.NAME, "submit_search")
    __CART_ICON = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a')
    __EXPANDED_CARD_POPUP = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/div')
    __CHECKOUT_CART_BUTTON = (By.XPATH, '//*[@id="button_order_cart"]/span')
    __5TH_DROPDOWN_ELEMENT = (By.XPATH, '//*[@id="index"]/div[2]/ul/li[5]')
    __CART_POPUP_PRODUCT_NUMBER = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1][text()="1"]')

    def search_field(self):
        return self.get_element(by_locator=self.__SEARCH_FIELD)

    def search_5th_dropdown_element(self):
        return self.get_element(by_locator=self.__5TH_DROPDOWN_ELEMENT)

    def fill_search_field(self, value):
        self.fill(by_locator=self.__SEARCH_FIELD, value=value)

    def click_search_button(self):
        self.click(by_locator=self.__SEARCH_BUTTON)

    def cart_icon(self):
        return self.get_element(by_locator=self.__CART_ICON)
        
    def mouse_over_cart_icon(self):
        cartIcon = self.cart_icon()
        action = ActionChains(self.driver)
        action.move_to_element(cartIcon).perform()

    def cart_popup_product_number(self):
        return self.get_element(by_locator=self.__CART_POPUP_PRODUCT_NUMBER)

    def expanded_cart_popup(self):
        return self.get_element(by_locator=self.__EXPANDED_CARD_POPUP)

    def click_checkout_cart(self):
        self.click(by_locator=self.__CHECKOUT_CART_BUTTON)