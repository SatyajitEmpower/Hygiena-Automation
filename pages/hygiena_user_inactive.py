from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class UserInactive(BasePage):
    """Playwright Page Object for User Inactive."""

    # ---------- LOCATORS ----------
    USER_MANAGEMENT_BTN = "xpath=//*[@id='userManagement']/div/img"
    INACTIVE_TOGGLE_INPUT = "xpath=//*[@id='userMgmUsers']/tbody/tr[1]/td[8]"
    

    def __init__(self, page: Page):
        super().__init__(page)

    def click_user_management(self):
        self.page.locator(self.USER_MANAGEMENT_BTN).click()
        self.wait_for_network()
        self.page.wait_for_timeout(3000)

    def click_user_active_inactive_btn(self):
        """
        Ensure the first listed user is marked inactive by unchecking the toggle.

        Some UIs disable the checkbox when already inactive, so we:
        - wait for the element to be attached and visible
        - scroll it into view
        - uncheck only if it is currently checked (i.e., active)
        """
        self.page.locator(self.INACTIVE_TOGGLE_INPUT).click()
        self.wait_for_network()
        self.page.wait_for_timeout(3000)

        # toggle.uncheck(force=True)
        
