from pages.hygiena_user_changepassword import UserPasswordupdate
from pages.hygiena_login_page import LoginPage
from pages.hygiena_user_update import UserUpdate

def test_user_password_update(page):
    # Login first
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()
    
    # Create user
    user_page = UserPasswordupdate(page)
    user_page.click_user_management()
    user_page.click_edit_user()
    user_page.click_change_password()
    user_page.PasswordUpdate("Test@1234", "Test@1234")

    # Print confirmation
    # print("Password change test completed successfully.")
