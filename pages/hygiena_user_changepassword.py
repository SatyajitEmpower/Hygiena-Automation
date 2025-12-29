from playwright.sync_api import Page
from pages.base_page import BasePage
import time


class UserPasswordupdate(BasePage):
    """Playwright Page Object for User Change Password - Update Password"""

    # ---------- LOCATORS ----------
    USER_MANAGEMENT = "#userManagement div img"
    EDITUSER_BTN = "#userMgmBtnEditUser"
    CHANGE_PASSWORD_BTN = "#changeUserPwdAccordinDiv"
    PASSWORD_FIELD = "#userPasswordInput"
    CONFIRM_PASSWORD_FIELD = "#userConfirmPwdInput"
    SAVE_USER_BTN = "#userMgmBtnSave"

    def __init__(self, page: Page):
        super().__init__(page)

    # ---------- ACTIONS ----------
    def click_user_management(self):
        time.sleep(1)
        self.page.locator(self.USER_MANAGEMENT).click()
        time.sleep(2)

    def click_edit_user(self):
        edit_btn = self.page.locator(self.EDITUSER_BTN).first
        edit_btn.scroll_into_view_if_needed()
        edit_btn.wait_for(state="visible", timeout=10000)
        edit_btn.click()
        time.sleep(2)

    # ---------- Click Change Password ----------
    def click_change_password(self):
        change_pwd_btn = self.page.locator(self.CHANGE_PASSWORD_BTN).first
        change_pwd_btn.scroll_into_view_if_needed()
        change_pwd_btn.wait_for(state="visible", timeout=10000)
        change_pwd_btn.click()
        time.sleep(2)

    # ---------- MAIN FLOW ----------
    def PasswordUpdate(self, user_password, user_confirm):

        # Password
        self.page.locator(self.PASSWORD_FIELD).fill(user_password)
        time.sleep(1)

        # Confirm Password
        self.page.locator(self.CONFIRM_PASSWORD_FIELD).fill(user_confirm)
        time.sleep(1)

        # Save
        self.page.locator(self.SAVE_USER_BTN).click()
        time.sleep(3)

        # Wait for completion
        self.wait_for_network()
        time.sleep(5)

        # Print confirmation after successful completion
        print("Password change test completed successfully.")
