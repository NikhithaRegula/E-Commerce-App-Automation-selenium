import time

from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver
        self.paybybankwire_button=(By.XPATH,"//a[@href='http://www.automationpractice.pl/index.php?fc=module&module=bankwire&controller=payment']")
        self.confirm_pay_button=(By.XPATH,"//button[@class='button btn btn-default button-medium']")

    def open_page(self, url):
        self.driver.get(url)

    def checkout(self):
        payment_button = self.driver.find_element(*self.paybybankwire_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", payment_button)
        payment_button.click()
        confirm_button=self.driver.find_element(*self.confirm_pay_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",confirm_button)
        confirm_button.click()