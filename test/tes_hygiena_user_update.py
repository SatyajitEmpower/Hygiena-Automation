from pages.hygiena_user_update import UserUpdate
from pages.hygiena_login_page import LoginPage

def test_user_update(page):
    # Login first
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()
    
    # Create user
    user_page = UserUpdate(page)
    user_page.click_user_management()
    user_page.click_edit_user()
    user_page.UserCreate("John", "Doe", "sambhu01", "sambhus@yopmail.com")
