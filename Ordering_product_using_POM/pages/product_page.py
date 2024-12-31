import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



class ProductPage:
    def __init__(self,driver):
        self.driver=driver
        self.women_hover=(By.XPATH,"//a[@href='http://www.automationpractice.pl/index.php?id_category=3&controller=category']")
        self.dress_type=(By.XPATH,"//a[@href='http://www.automationpractice.pl/index.php?id_category=11&controller=category']")
        self.select_dress=(By.CLASS_NAME,"left-block")
        self.colorchange=(By.ID,"color_11")
        self.cart_button=(By.XPATH,"//button[@class='exclusive']")
        self.proceed_button=(By.XPATH,"//a[@href='http://www.automationpractice.pl/index.php?controller=order']")


    def open_page(self,url):
        self.driver.get(url)

    def product_menu(self):
        women_element = self.driver.find_element(*self.women_hover)
        actions = ActionChains(self.driver)
        actions.move_to_element(women_element).perform()
        self.driver.find_element(*self.dress_type).click()
        dress_element = self.driver.find_element(*self.select_dress)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dress_element)
        dress_element.click()
        time.sleep(2)
        color=self.driver.find_element(*self.colorchange)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", color)
        color.click()
        self.driver.find_element(*self.cart_button).click()
        self.driver.find_element(*self.proceed_button).click()


