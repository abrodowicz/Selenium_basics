import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.authentication_page import AuthenticationPage
from pages.header_section import HeaderSection
from pages.search_section import SearchSection
from pages.search_page import SearchPage
from pages.summary_page import SummaryPage
from pages.sign_up_form import SignUpPage
from pages.account_page import AccountPage


class TestSelenium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.header_section = HeaderSection()
        self.authentication_page = AuthenticationPage()
        self.search_section = SearchSection()
        self.search_page = SearchPage()
        self.summary_page = SummaryPage()
        self.sign_up_form = SignUpPage()
        self.account_page = AccountPage()
        self.authentication_page.go_to_url(url="http://automationpractice.com/index.php")

    def test_search_by_valid_data(self):
        # Step_1. Type something in search field on the header of the page
        self.search_section.search_field().send_keys("Printed dress")
        # Step_2. Verify that 5 goods are presented in the elastic search dropdown
        self.assertTrue(self.search_section.search_5th_dropdown_element())
        # Step_3. Click Search button on the header of the page
        self.search_section.click_search_button()
        # Step_4. Verify that search results block is presented
        self.assertTrue(self.search_page.search_page_title())
        # Step_5. Verify that 5 goods are presented in results block
        self.assertTrue(self.search_page.search_5th_product())

    def test_registration_with_correct_data(self):
        # Step_1. Click Sign in button on the header of the page
        self.header_section.click_sign_in_button()
        # Step_2. Submit Create an account form on Authentication page
        self.authentication_page.sign_in_to_application()
        # Step_3. Fill in sign up form
        self.assertTrue(self.authentication_page.authentication_page_title())
        self.sign_up_form.fill_firstname_field()
        self.sign_up_form.fill_lastname_field()
        self.sign_up_form.fill_password_field()
        self.sign_up_form.fill_address1_field()
        self.sign_up_form.fill_city_field()
        self.sign_up_form.open_state_dropdown()
        self.sign_up_form.choose_dropdown()
        self.sign_up_form.fill_postcode_field()
        self.sign_up_form.fill_phone_field()
        # Step_4. Submit sign up form
        self.sign_up_form.submit_account_button()
        # Step_5. Check nickname is displayed on the header of the page
        self.assertTrue(self.header_section.check_if_nickname_is_presented())
        # Step_6. Verify that My account block is presented
        self.assertTrue(self.account_page.account_page_title())
        # Step_7. Click logout button on the header of the page
        self.header_section.click_logout_button()

    def test_add_to_cart(self):
        # Step_1. Type something in search field on the header of the page
        self.search_section.fill_search_field("Dress")
        # Step_2. Click Search button on the header of the page
        self.search_section.click_search_button()
        # Step_3. Verify that search results block is presented
        self.assertTrue(self.search_page.search_page_title())
        # Step_4. Verify that at least 1 good is presented in result block
        self.assertTrue(self.search_page.search_result_item())
        # Step_5. Click Add to cart button for any good from result block
        self.search_page.add_item_to_cart()
        # Step_6. Verify that adding to card confirmation popup is presented on the page
        self.assertTrue(self.search_page.confirmation_popup())
        # Step_7. Close adding to card confirmation popup
        self.search_page.close_confirmation_popup()
        # Step_8. Hover mouse cursor on “Cart“ icon
        self.search_section.mouse_over_cart_icon()
        # Step_9. Verify that expanded Cart popup is presented
        self.assertTrue(self.search_section.expanded_cart_popup())
        # Step_10. Verify that 1 good is presented in Cart popup
        self.assertTrue(self.search_section.cart_popup_product_number())
        # Step_11. Click Check out button in expanded Cart popup
        self.search_section.click_checkout_cart()
        # Step_12. Verify that shopping-cart summary page is presenting
        self.assertTrue(self.summary_page.summary_page_title())
        # Step_13. Verify that 1 good is presented on shopping-cart summary page
        self.assertTrue(self.summary_page.summary_page_product_quantity())
        # Step_14. Click Trash icon on shopping-cart summary page
        self.summary_page.click_trash_icon()

    def tearDown(self) -> None:
        self.authentication_page.quit_driver()


if __name__ == "__main__":
    unittest.main()