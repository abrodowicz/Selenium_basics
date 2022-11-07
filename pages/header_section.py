from selenium.webdriver.common.by import By


class HeaderSection:

    def _init_(self, driver):
        self.driver = driver

    def click_sign_in_button(self):
        self.driver.find_element(By.XPATH, '//a[@title="Log in to your customer account"]').click()

    def check_if_nickname_is_presented(self):
        return self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span[text()="Tester Testowy"]')

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a').click()