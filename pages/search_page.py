from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    __SEARCH_PAGE_TITLE = (By.XPATH, '//div/span[text()="Search"]')
    __PURCHASE_CONFIRMATION_POPUP = (By.ID, 'layer_cart')
    __CLOSE_BUTTON_FOR_CONFIRMATION_POPUP = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/span')
    __SEARCH_RESULT_ITEM = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div')
    __ADD_BUTTON_FOR_SEARCH_RESULT_ITEM = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]')

    # dynamic xpaths
    __PRODUCT = (By.XPATH, '//*[@id="center_column"]/ul/li[{index}]')

    def check_if_search_block_contains_element(self, expected_product_quantity: int) -> bool:
        element_locator = (By.XPATH, self.__PRODUCT.format(index=expected_product_quantity))
        self.if_element_present(by_locator=element_locator)

    def search_page_title(self):
        self.if_element_present(by_locator=self.__SEARCH_PAGE_TITLE)

    def search_result_item(self):
        self.if_element_present(by_locator=self.__SEARCH_RESULT_ITEM)

    def add_item_to_cart(self):
        itemBox = self.get_element(by_locator=self.__SEARCH_RESULT_ITEM)
        act = ActionChains(self.driver)
        act.move_to_element(itemBox).perform()
        self.click(by_locator=self.__ADD_BUTTON_FOR_SEARCH_RESULT_ITEM)

    def confirmation_popup(self):
        self.if_element_present(by_locator=self.__PURCHASE_CONFIRMATION_POPUP)

    def close_confirmation_popup(self):
        self.click(by_locator=self.__CLOSE_BUTTON_FOR_CONFIRMATION_POPUP)
