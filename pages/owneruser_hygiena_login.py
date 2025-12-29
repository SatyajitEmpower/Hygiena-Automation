from pages.base_page import BasePage
from config.config import config
class OwnerUserLoginPage(BasePage):
    OwnerUser_username = "#UserName"
    OwnerUser_password = "#Password"
    LOGIN_BUTTON = "#loginButton"
    def open(self):
        self.page.goto(config.LOGIN_URL)
        self.wait_for_network()
        # Wait for login form to be visible
        self.expect_visible(self.OwnerUser_username)
        self.page.wait_for_timeout(2000)  # Wait 2 seconds for page to fully load
    def OwnerUserLogin(self):
        self.fill(self.OwnerUser_username, config.OwnerUser_username)
        self.fill(self.OwnerUser_password, config.OwnerUser_password)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_network()
        # Wait for dashboard to load
        self.page.wait_for_url(config.DASHBOARD_URL, timeout=10000)
        self.page.wait_for_timeout(20000)
