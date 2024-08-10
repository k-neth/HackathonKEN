import pytest
from pages.login_page import LoginPage
from utils.data_reader import get_test_data

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        test_data = get_test_data("data/test_data.json")

        login_page.enter_username(test_data["valid_user"]["username"])
        login_page.enter_password(test_data["valid_user"]["password"])
        login_page.click_login()

        assert "Dashboard" in driver.title

    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        test_data = get_test_data("data/test_data.json")

        login_page.enter_username(test_data["invalid_user"]["username"])
        login_page.enter_password(test_data["invalid_user"]["password"])
        login_page.click_login()

        assert "Invalid credentials" in driver.page_source
