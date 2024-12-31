from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.signin_button = (By.CLASS_NAME, "login")
        self.email_Textbox=(By.ID, "email")
        self.password_Textbox=(By.ID, "passwd")
        self.login_button=(By.ID, "SubmitLogin")

    def open_page(self,url):
        self.driver.get(url)

    def user_login(self,email_id,password1):
        self.driver.find_element(*self.signin_button).click()
        self.driver.find_element(*self.email_Textbox).send_keys(email_id)
        self.driver.find_element(*self.password_Textbox).send_keys(password1)
        self.driver.find_element(*self.login_button).click()
