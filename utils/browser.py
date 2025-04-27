# utils/browser.py
from selenium import webdriver

class Browser:
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()

        self.driver.get('https://backend.yclmall.com/admin/login.jsp')
        self.driver.implicitly_wait(10)  # 隐式等待

    def quit(self):
        self.driver.quit()