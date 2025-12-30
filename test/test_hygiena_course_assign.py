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
    time.sleep(1)

    # ensure quantity inputs are active
    user_page.click_fht_course_quantity()
    user_page.click_fmt_course_quantity()

    # assign users and due dates before going to payment (avoids footer overlay)
    user_page.assign_fht_user("John Doe")
    user_page.assign_fmt_user("John Doe")
    user_page.set_due_date_fht("2024-12-31")

    # proceed to purchase after assignments are completed
    user_page.click_buy_now()
    user_page.click_complete_purchase()
