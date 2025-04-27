# testcases/test_login.py
import pytest
from pages.login_page import LoginPage
from utils.browser import Browser

@pytest.fixture(scope="module")
def setup():
    driver = Browser().driver
    yield driver
    driver.quit()

def test_login_success(setup):
    login_page = LoginPage(setup)
    login_page.login("ZhongFuCheng", "Zfc%#1025")
    print(setup.title)
    assert "管理中心" in setup.title