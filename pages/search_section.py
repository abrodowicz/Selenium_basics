from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchSection(BasePage):

    __SEARCH_FIELD = (By.ID, "search_query_top")
    __SEARCH_BUTTON = (By.NAME, "submit_search")
    __CART_ICON = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a')
    __EXPANDED_CARD_POPUP = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/div')
    __CHECKOUT_CART_BUTTON = (By.XPATH, '//*[@id="button_order_cart"]/span')

    # dynamic xpaths
    __DROPDOWN_ELEMENT = (By.XPATH, '//*[@id="index"]/div[2]/ul/li[{index}]')
    __CART_POPUP_PRODUCT_NUMBER = (By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1][text()="{index}"]')

    def fill_search_field(self, search_phrase: str) -> None:
        self.fill(by_locator=self.__SEARCH_FIELD, value=search_phrase)

    def check_if_dropdown_contains_element(self, expected_element_number: int) -> bool:
        element_locator = (By.XPATH, self.__DROPDOWN_ELEMENT.format(index=expected_element_number))
        self.if_element_present(by_locator=element_locator)

    def click_search_button(self):
        self.click(by_locator=self.__SEARCH_BUTTON)

    def cart_icon(self):
        return self.get_element(by_locator=self.__CART_ICON)
        
    def mouse_over_cart_icon(self):
        cartIcon = self.cart_icon()
        action = ActionChains(self.driver)
        action.move_to_element(cartIcon).perform()

    def check_cart_popup_product_number(self, expected_product_number: int) -> bool:
        element_locator = (By.XPATH, self.__CART_POPUP_PRODUCT_NUMBER.format(index=expected_product_number))
        self.if_element_present(by_locator=element_locator)

    def expanded_cart_popup(self):
        self.if_element_present(by_locator=self.__EXPANDED_CARD_POPUP)

    def click_checkout_cart(self):
        self.click(by_locator=self.__CHECKOUT_CART_BUTTON)
