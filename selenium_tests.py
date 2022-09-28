import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
import string
from selenium.webdriver.support.select import Select


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


class TestSelenium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(5)

    def test_search_by_valid_data(self):
        self.driver.get(url="http://automationpractice.com/index.php")
        self.driver.find_element(By.ID, "search_query_top").send_keys("Printed dress")
        time.sleep(20)
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="index"]/div[2]/ul/li[5]'))
        self.driver.find_element(By.NAME, "submit_search").click()
        self.assertTrue(self.driver.find_element(By.XPATH, '//div/span[text()="Search"]'))
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[5]'))

    def test_registration_with_correct_data(self):
        self.driver.get(url="http://automationpractice.com/index.php")
        self.driver.find_element(By.XPATH, '//a[@title="Log in to your customer account"]').click()
        self.driver.find_element(By.ID, 'email_create').send_keys(random_char(7)+"@gmail.com")
        self.driver.find_element(By.XPATH, '//*[@id="SubmitCreate"]').click()
        time.sleep(10)
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="columns"]/div[1]/span[2][text()="	Authentication"]'))
        self.driver.find_element(By.ID, 'customer_firstname').send_keys("Tester")
        self.driver.find_element(By.ID, 'customer_lastname').send_keys("Testowy")
        self.driver.find_element(By.ID, 'passwd').send_keys("Password123!")
        self.driver.find_element(By.ID, 'address1').send_keys("PO Box 515381")
        self.driver.find_element(By.ID, 'city').send_keys("Los Angeles")
        self.driver.find_element(By.XPATH, '//*[@id="id_state"]').click()
        dropdown = Select(self.driver.find_element(By.XPATH, '//*[@id="id_state"]'))
        dropdown.select_by_value("1")
        self.driver.find_element(By.ID, 'postcode').send_keys("90001")
        self.driver.find_element(By.ID, 'phone_mobile').send_keys("123456789")
        self.driver.find_element(By.XPATH, '//*[@id="submitAccount"]/span').click()
        time.sleep(10)
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span[text()="Tester Testowy"]'))
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="columns"]/div[1]/span[2][text()="My account"]'))
        self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a').click()

    def test_add_to_cart(self):
        self.driver.get(url="http://automationpractice.com/index.php")
        self.driver.find_element(By.ID, "search_query_top").send_keys("Dress")
        self.driver.find_element(By.NAME, "submit_search").click()
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="columns"]/div[1]/span[2][text()="Search"]'))
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div'))
        itemBox = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div')
        act = ActionChains(self.driver)
        act.move_to_element(itemBox).perform()
        self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]').click()
        self.assertTrue(self.driver.find_element(By.ID, 'layer_cart'))
        time.sleep(15)
        self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/span').click()
        cartIcon = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a')
        act.move_to_element(cartIcon).perform()
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/div'))
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1][text()="1"]'))
        self.driver.find_element(By.XPATH, '//*[@id="button_order_cart"]/span').click()
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="columns"]/div[1]/span[2][text()="Your shopping cart"]'))
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[@id="summary_products_quantity"][text()="1 Product"]'))
        self.driver.find_element(By.XPATH, '//*[@id="5_19_0_0"]/i').click()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()