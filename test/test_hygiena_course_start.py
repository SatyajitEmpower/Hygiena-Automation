from pages.hygiena_course_start import CourseStart
from pages.hygiena_login_page import LoginPage

def test_user_create(page):
    # Login first
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()
    
    # Assign course
    
    user_page = CourseStart(page)
    user_page.click_elearning()
    user_page.click_course()
    user_page.click_start_course()