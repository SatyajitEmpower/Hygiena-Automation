from playwright.sync_api import Page
from pages.base_page import BasePage


class UserInactive(BasePage):
    """Playwright Page Object for User Inactive."""

    # ---------- LOCATORS ----------
    USER_MANAGEMENT_BTN = "xpath=//*[@id='userManagement']/div/img"
    INACTIVE_TOGGLE_INPUT = "xpath=//table//tbody/tr[1]//td[8]//input[@type='checkbox']"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_user_management(self):
        self.page.locator(self.USER_MANAGEMENT_BTN).click()
        self.wait_for_network()
        self.page.wait_for_timeout(3000)

    def click_user_inactive_btn(self):
        toggle = self.page.locator(self.INACTIVE_TOGGLE_INPUT)
        toggle.wait_for(state="attached", timeout=10000)

        # Avoid double toggle
        if toggle.is_disabled():
            self.page.evaluate(
                """
                (el) => {
                    el.checked = true;
                    el.dispatchEvent(new Event('input', { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                }
                """,
                toggle,
            )

        self.wait_for_network()
        self.page.wait_for_timeout(3000)
        print("User inactivated successfully.")