from selenium.webdriver.common.by import By
class User:
    num = 0

    def __init__(self,name):
        self.username_input = (By.ID, "username")
        User.num += 1

    def addUser(self):
        print(*self.username_input)
        print(User.num)

u = User('张三')
u.addUser()

