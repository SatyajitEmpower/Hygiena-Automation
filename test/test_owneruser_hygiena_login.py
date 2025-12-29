from pages.owneruser_hygiena_login import OwnerUserLoginPage
def test_login(page):
    login_page = OwnerUserLoginPage(page)
    # Login
    login_page.open()
    login_page.OwnerUserLogin()