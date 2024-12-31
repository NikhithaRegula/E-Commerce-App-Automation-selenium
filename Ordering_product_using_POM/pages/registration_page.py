from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self,driver):
        self.driver=driver
        self.signin_button=(By.CLASS_NAME, "login")
        self.email_textbox = (By.ID, "email_create")
        self.create_account_button=(By.ID,"SubmitCreate")
        self.gender_button=(By.ID,"id_gender2")
        self.firstname_textbox = (By.ID, "customer_firstname")
        self.lastname_textbox = (By.ID, "customer_lastname")
        self.password_textbox = (By.ID, "passwd")
        self.register_button =(By.ID,"submitAccount")

    def open_page(self, url):
        self.driver.get(url)

    def newuser_registration(self,email,firstname,lastname,password):
        self.driver.find_element(*self.signin_button).click()
        self.driver.find_element(*self.email_textbox).send_keys(email)
        self.driver.find_element(*self.create_account_button).click()
        self.driver.find_element(*self.gender_button).click()
        self.driver.find_element(*self.firstname_textbox).send_keys(firstname)
        self.driver.find_element(*self.lastname_textbox).send_keys(lastname)
        self.driver.find_element(*self.password_textbox).send_keys(password)
        self.driver.find_element(*self.register_button).click()
