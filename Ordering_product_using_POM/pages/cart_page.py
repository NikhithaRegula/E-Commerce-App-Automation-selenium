import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self,driver):
        self.driver=driver
        self.cart_proceed_button=(By.XPATH,"//a[@href='http://www.automationpractice.pl/index.php?controller=order&step=1']")
        # self.address_textbox=(By.ID,"address1")
        # self.city_box=(By.ID,"city")
        # self.dropdown_state=(By.ID,"id_state")
        # self.postalcode_textbox=(By.ID,"postcode")
        # self.homephone_textbox=(By.ID,"phone")
        # self.save_button=(By.ID,"submitAddress")
        self.proceed_address_button= (By.NAME,"processAddress")
        self.terms_check_box=(By.ID,"cgv")
        self.proceed_shipping_button=(By.NAME,"processCarrier")

    def open_page(self,url):
        self.driver.get(url)

    def cart(self,useraddress,city,zipcode,homephone):
        button_cart = self.driver.find_element(*self.cart_proceed_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button_cart)
        button_cart.click()
        # address_box=self.driver.find_element(*self.address_textbox)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", address_box)
        # address_box.send_keys(useraddress)
        # self.driver.find_element(*self.city_box).send_keys(city)
        #
        # dropdown = self.driver.find_element(*self.dropdown_state)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(dropdown).click().perform()
        # # Scroll by sending down arrow key several times
        # for _ in range(33):
        #     actions.send_keys(Keys.ARROW_DOWN).perform()

        # self.driver.find_element(*self.postalcode_textbox).send_keys(zipcode)
        # self.driver.find_element(*self.homephone_textbox).send_keys(homephone)
        # self.driver.find_element(*self.save_button).click()

        proceed_with_address = self.driver.find_element(*self.proceed_address_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", proceed_with_address)
        proceed_with_address.click()

        check_box = self.driver.find_element(*self.terms_check_box)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", check_box)
        check_box.click()
        self.driver.find_element(*self.proceed_shipping_button).click()

