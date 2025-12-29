from playwright.sync_api import Page, expect
class BasePage:
    def __init__(self, page: Page):
        self.page = page
    def click(self, selector: str):
        self.page.locator(selector).click()
    def force_click(self, selector: str):
        self.page.locator(selector).click(force=True)
    def fill(self, selector: str, value: str):
        self.page.locator(selector).fill(value)
    def wait_for_network(self):
        self.page.wait_for_load_state("networkidle")
    def expect_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()