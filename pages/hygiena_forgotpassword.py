from pages.base_page import BasePage
from config.config import config
class ForgotPassword(BasePage):
    Forgot_Username_Password = "#Username"
    Next_BUTTON = "xpath=/html/body/platform-root/platform-auth-layout/div/div/div/platform-forget-password/section/form/div[3]/div/button"
    def open(self):
        self.page.goto(config.ForgotPassword_url)
        self.wait_for_network()
        # Wait for login form to be visible
        self.expect_visible(self.Forgot_Username_Password)
        self.page.wait_for_timeout(2000)  # Wait 2 seconds for page to fully load
    def Forgot(self):
        self.fill(self.Forgot_Username_Password, config.ForgotEmail)
        self.click(self.Next_BUTTON)
        self.wait_for_network()
        self.page.wait_for_timeout(2000)  # Wait 2 seconds for page to fully load