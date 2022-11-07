from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class SignUpPage(BasePage):

    __FIRSTNAME_FIELD = (By.ID, 'customer_firstname')
    __LASTNAME_FIELD = (By.ID, 'customer_lastname')
    __PASSWORD_FIELD = (By.ID, 'passwd')
    __ADDRESS1_FIELD = (By.ID, 'address1')
    __CITY_FIELD = (By.ID, 'city')
    __STATE_DROPDOWN_ARROW = (By.XPATH, '//*[@id="uniform-id_state"]')
    __DROPDOWN_FIELD = (By.XPATH, '//*[@id="id_state"]')
    __POSTCODE_FIELD = (By.ID, 'postcode')
    __PHONE_FIELD = (By.ID, 'phone_mobile')
    __SUBMIT_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="submitAccount"]/span')

    def fill_firstname_field(self):
        self.fill(by_locator=self.__FIRSTNAME_FIELD, value="Tester")

    def fill_lastname_field(self):
        self.fill(by_locator=self.__LASTNAME_FIELD, value="Testowy")

    def fill_password_field(self):
        self.fill(by_locator=self.__PASSWORD_FIELD, value="Password123!")

    def fill_address1_field(self):
        self.fill(by_locator=self.__ADDRESS1_FIELD, value="PO Box 515381")

    def fill_city_field(self):
        self.fill(by_locator=self.__CITY_FIELD, value="Los Angeles")

    def open_state_dropdown(self):
        self.click(by_locator=self.__STATE_DROPDOWN_ARROW)

    def choose_dropdown(self):
        dropdown = Select(self.get_element(by_locator=self.__DROPDOWN_FIELD))
        dropdown.select_by_value("1")

    def fill_postcode_field(self):
        self.fill(by_locator=self.__POSTCODE_FIELD, value="90001")

    def fill_phone_field(self):
        self.fill(by_locator=self.__PHONE_FIELD, value="123456789")

    def submit_account_button(self):
        self.click(by_locator=self.__SUBMIT_ACCOUNT_BUTTON)