from pages.Owneruser_hygiena_course_start import OwnerUserCourseStart
from pages.owneruser_hygiena_login import OwnerUserLoginPage

def test_course_start(page):
    # Login first
    login_page = OwnerUserLoginPage(page)
    login_page.open()
    login_page.OwnerUserLogin()

    # Assign course
    
    user_page = OwnerUserCourseStart(page)
    user_page.click_elearning()
    user_page.click_start_course()