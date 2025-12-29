from playwright.sync_api import Page
from pages.base_page import BasePage


class UesrRemove(BasePage):
    """Playwright Page Object for course Start."""

    # ---------- LOCATORS ----------
    Usermanagement_btn = "xpath=//*[@id='userManagement']/div/img"
    Delete_btn = "xpath=//*[@id='userMgmBtnDeleteUser']"
    Confirnm_delete_btn = "xpath=/html/body/div/div/div/div[3]/div/div[2]/div[1]/div/div/div"
    Cancel_delete_btn = "xpath=/html/body/div/div/div/div[3]/div/div[2]/div[2]/div/div/div"

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

    # ---------- Click user delete confirm btn ----------

    def click_confirm_delete_btn(self):
        confirm_delete_btn = self.page.locator(self.Confirnm_delete_btn).first
        confirm_delete_btn.scroll_into_view_if_needed()
        confirm_delete_btn.wait_for(state="visible", timeout=10000)
        confirm_delete_btn.click()
        self.wait_for_network()
        self.page.wait_for_timeout(5000)

    # ---------- Don't click user delete confirm btn ----------

    # def click_cancel_delete_btn(self):
    #     cancel_delete_btn = self.page.locator(self.Cancel_delete_btn).first
    #     cancel_delete_btn.scroll_into_view_if_needed()
    #     cancel_delete_btn.wait_for(state="visible", timeout=10000)
    #     cancel_delete_btn.click()
    #     self.wait_for_network()
    #     self.page.wait_for_timeout(5000)

        # Print confirmation after successful completion
        print("User deletion process initiated successfully.")

