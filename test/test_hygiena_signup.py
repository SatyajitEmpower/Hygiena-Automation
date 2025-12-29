import time
from pages.hygiena_signup_page import SignupPage
def test_signup(page):
    signup_page = SignupPage(page)
    # Signup
    signup_page.open()
    signup_page.signup(captcha_timeout=5000)  
    
    # Short timeout for testing
    signup_page.wait_for_captcha_solution(timeout=5000)
    # Verify successful signup by checking for a welcome message or dashboard element
    time.sleep(5000)  # Wait for potential redirection after signup