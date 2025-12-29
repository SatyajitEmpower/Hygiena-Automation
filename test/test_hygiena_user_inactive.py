from pages.hygiena_user_inactive import UserInactive
from pages.hygiena_login_page import LoginPage


def test_user_inactive(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()

    user_page = UserInactive(page)
    user_page.click_user_management()
    user_page.click_user_inactive_btn()
