from playwright.sync_api import Page
from pages.base_page import BasePage
import time


class UserManagementCreate(BasePage):
    """Playwright Page Object for User Management - Create User"""

    # ---------- LOCATORS ----------
    USER_MANAGEMENT = "#userManagement div img"
    ADD_USER_BTN = "#addUserLink"
    USER_FIRSTNAME = "#userMgmFirstName"
    USER_LASTNAME = "#userMgmLastName"
    USER_USERNAME = "#userMgmUserName"
    USER_EMAIL = "#userMgmEmail"
    USER_ROLE_DROPDOWN = "#userMgmRoleNames"
    SAVE_USER_BTN = "#userMgmBtnSave"

    def __init__(self, page: Page):
        super().__init__(page)

    # ---------- ACTIONS ----------
    def click_user_management(self):
        time.sleep(1)
        self.page.locator(self.USER_MANAGEMENT).click()
        time.sleep(2)

    def click_add_user(self):
        self.page.locator(self.ADD_USER_BTN).click()
        time.sleep(2)

    # ---------- HELPERS ----------
    def select_dropdown_by_text(self, locator, text):
        time.sleep(1)
        dropdown = self.page.locator(locator)
        dropdown.select_option(label=text)
        time.sleep(1)

    # ---------- MAIN FLOW ----------
    def UserCreate(self, user_first_name, user_last_name, user_name, user_email):

        # First Name
        self.page.locator(self.USER_FIRSTNAME).fill(user_first_name)
        time.sleep(1)

        # Last Name
        self.page.locator(self.USER_LASTNAME).fill(user_last_name)
        time.sleep(1)

        # Username
        self.page.locator(self.USER_USERNAME).fill(user_name)
        time.sleep(1)

        # Email
        self.page.locator(self.USER_EMAIL).fill(user_email)
        time.sleep(1)

        # Role
        self.select_dropdown_by_text(self.USER_ROLE_DROPDOWN, "SureTrend User")

        # Save
        self.page.locator(self.SAVE_USER_BTN).click()
        time.sleep(3)

        # Wait for completion
        self.wait_for_network()
        time.sleep(5)
