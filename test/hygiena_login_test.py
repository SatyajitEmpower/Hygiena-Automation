from pages.hygiena_login_page import LoginPage
def test_login(page):
    login_page = LoginPage(page)
    # Login
    login_page.open()
    login_page.login()

    