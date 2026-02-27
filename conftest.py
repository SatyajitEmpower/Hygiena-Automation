import pytest
from playwright.sync_api import sync_playwright
from config.config import config

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config.headless)
    #   browser = p.firefox.launch(headless=config.headless)
    #   browser = p.webkit.launch(headless=config.headless)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()