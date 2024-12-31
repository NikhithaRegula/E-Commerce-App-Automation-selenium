import time
import pytest
from selenium import webdriver
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from Ordering_product_using_POM.pages.registration_page import RegistrationPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("email,firstname,lastname,password",[
    ("fight@gmail.com","Never","Stop","Learning@15")
])


def test_registration(driver,email,firstname,lastname,password):

    registration_page=RegistrationPage(driver)
    registration_page.open_page("http://www.automationpractice.pl/index.php")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "login")))
    registration_page.newuser_registration(email,firstname,lastname,password)
    time.sleep(5)