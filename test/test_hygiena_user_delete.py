from pages.hygiena_user_delete import UesrRemove
from pages.hygiena_login_page import LoginPage

def test_user_create(page):
    # Login first
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()
    
    # Assign course
    
    user_page = UesrRemove(page)
    user_page.click_user_management()
    user_page.click_user_delete_btn()
    