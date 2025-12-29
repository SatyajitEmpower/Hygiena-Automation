from playwright.sync_api import Page
from pages.base_page import BasePage


class OwnerUserCourseStart(BasePage):
    """Playwright Page Object for course Start."""

    # ---------- LOCATORS ----------
    ELearning_btn = "#elearningSpan"
    Course_start_btn = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div/app-courses-grid/div/div[2]/table/tbody/tr[1]/td[9]/button"
    # Course_resume_btn = "button:has-text('Resume')"

    def __init__(self, page: Page):
        super().__init__(page)

    # ---------- Click E-Learning btn ----------

    def click_elearning(self):
        self.page.locator(self.ELearning_btn).click()
        self.wait_for_network()
        self.page.wait_for_timeout(5000)

    # ---------- Click Start or Resume Course button ----------

    def click_start_course(self):
        # Try to click Start button first
        try:
            start_btn = self.page.locator(self.Course_start_btn).first
            start_btn.scroll_into_view_if_needed()
            start_btn.wait_for(state="visible", timeout=5000)
            start_btn.click()
        except:
            # If Start button not found, click Resume button
            resume_btn = self.page.locator(self.Course_resume_btn).first
            resume_btn.scroll_into_view_if_needed()
            resume_btn.wait_for(state="visible", timeout=5000)
            resume_btn.click()
        
        self.page.wait_for_timeout(5000)  # Wait for course to load

        # Print confirmation after successful completion
        print("Course started or resumed successfully.")

    
        