import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from Ordering_product_using_POM.pages.cart_page import CartPage
from Ordering_product_using_POM.pages.checkout_page import CheckoutPage
from Ordering_product_using_POM.pages.login_page import LoginPage
from Ordering_product_using_POM.pages.product_page import ProductPage
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()
@pytest.mark.parametrize("email_id,password1",[
    ("fight@gmail.com","Learning@15")
])
@pytest.mark.parametrize("useraddress,city,zipcode,homephone",[
    ("339 1st ave, Newyork","manhattan","10005","243557968")
])

def test_login(driver,email_id,password1,useraddress,city,zipcode,homephone):
    login_page=LoginPage(driver)
    product_page=ProductPage(driver)
    cart_page=CartPage(driver)
    checkout_page=CheckoutPage(driver)
    login_page.open_page("http://www.automationpractice.pl/index.php")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,"login")))
    login_page.user_login(email_id,password1)
    product_page.product_menu()
    cart_page.cart(useraddress,city,zipcode,homephone)
    checkout_page.checkout()
    assert "Your order on My Shop is complete." in driver.page_source

    time.sleep(10)


