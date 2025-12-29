from pages.hygiena_course_assign import CourseAssign
from pages.hygiena_login_page import LoginPage
import time

def test_user_create(page):
    # Login first
    login_page = LoginPage(page)
    login_page.open()
    login_page.login()
    
    # Assign course
    
    user_page = CourseAssign(page)
    user_page.click_elearning()
    user_page.click_course_tab()
    user_page.select_both_courses()
    time.sleep(1000)  # wait for UI to update

    # user_page.select_fmt_course()
    # proceed to purchase to reveal quantity controls
    # user_page.select_fht_course_quantity(1)
    # user_page.select_fmt_course_quantity(1)
    # user_page.click_buy_now()
    # user_page.click_complete_purchase()
    # assign and set due date if needed
    # user_page.assign_fht_user("StageDec Twelve")
    # user_page.set_due_date_fht("2024-12-31")