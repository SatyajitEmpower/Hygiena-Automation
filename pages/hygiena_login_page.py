from pages.base_page import BasePage
from config.config import config
class LoginPage(BasePage):
    USERNAME = "#UserName"
    PASSWORD = "#Password"
    LOGIN_BUTTON = "#loginButton"
    def open(self):
        self.page.goto(config.LOGIN_URL)
        self.wait_for_network()
        # Wait for login form to be visible
        self.expect_visible(self.USERNAME)
        self.page.wait_for_timeout(2000)  # Wait 2 seconds for page to fully load
    def login(self):
        self.fill(self.USERNAME, config.USERNAME)
        self.fill(self.PASSWORD, config.PASSWORD)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_network()
        # Wait for dashboard to load
        self.page.wait_for_url(config.DASHBOARD_URL, timeout=10000)
        self.page.wait_for_timeout(20000)  # Wait 2 seconds for dashboard to fully load
