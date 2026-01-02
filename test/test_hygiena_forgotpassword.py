from pages.hygiena_forgotpassword import ForgotPassword
def test_forgot_password(page):
    forgot_password_page = ForgotPassword(page)
    # Forgot Password
    forgot_password_page.open()
    forgot_password_page.Forgot()