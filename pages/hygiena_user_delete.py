from playwright.sync_api import Page
from pages.base_page import BasePage


class UesrRemove(BasePage):
    """Playwright Page Object for course Start."""

    # ---------- LOCATORS ----------
    Usermanagement_btn = "xpath=//*[@id='userManagement']/div/img"
    Delete_btn = "xpath=//*[@id='userMgmBtnDeleteUser']"

    def __init__(self, page: Page):
        super().__init__(page)

    # ---------- Click E-Learning btn ----------

    def click_user_management(self):
        self.page.locator(self.Usermanagement_btn).click()
        self.wait_for_network()
        self.page.wait_for_timeout(5000)

    # ---------- Click Course tab ----------

    def click_user_delete_btn(self):
        delete_btn = self.page.locator(self.Delete_btn).first
        delete_btn.scroll_into_view_if_needed()
        delete_btn.wait_for(state="visible", timeout=10000)
        delete_btn.click()
        self.wait_for_network()
        self.page.wait_for_timeout(3000)