from pages.hygiena_usermanagement import UserManagementCreate
from pages.hygiena_login_page import LoginPage

def test_user_create(page):
    # Login first
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()
    
    # Create user
    user_page = UserManagementCreate(page)
    user_page.click_user_management()
    user_page.click_add_user()
    user_page.UserCreate("John", "Doe", "sambhu01", "sambhu@yopmail.com")
