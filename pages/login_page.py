# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")

    def login(self, username, password):
        self.driver.find_element(By.XPATH,'//button[@data-tab="user"]').click()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "loginButton").click()