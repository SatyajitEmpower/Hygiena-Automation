from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from config.config import config


class SignupPage:
    def __init__(self, page: Page):
        self.page = page

        # ---------- LOCATORS ----------
        self.Firstname = "#FirstName"
        self.Lastname = "#LastName"
        self.Username = "#UserName"

        self.WhatIndustry = "#Industry"
        self.SpecifyIndustry = "#Segment"
        self.CompanyName = "#CompanyName"

        self.SelectCountry = "#CountryId"
        self.Selectjobtitle = "#JobTitle"

        self.PhoneNumber = "#PhoneNumber"
        self.Email = "#Email"
        self.NextBtn = "#btnNext"

        self.CompanyAddress = "#Address"
        self.City = "#City"
        self.State = "#DistrictState"
        self.Zipcode = "#PostalCode"

        self.Term_and_Conditions = "#agreeCheckBox"

        # ---------- reCAPTCHA ----------
        self.RecaptchaFrame = "iframe[title*='reCAPTCHA'], iframe[src*='recaptcha']"
        self.RecaptchaCheckbox = "#recaptcha-anchor"
        self.CreateAccountBtn = "#btnReg"

    # ---------- PAGE LOAD ----------
    def open(self):
        self.page.goto(config.REGISTER_URL)
        self.page.wait_for_load_state("networkidle")
        self.page.locator(self.Firstname).wait_for(state="visible", timeout=10000)
        self.page.wait_for_timeout(1000)

    # ---------- DROPDOWN ----------
    def select_dropdown_by_text(self, selector: str, text: str):
        text = (text or "").strip()
        if not text:
            return

        try:
            self.page.select_option(selector, label=text)
        except Exception:
            options = self.page.locator(f"{selector} option")
            for i in range(options.count()):
                if text.lower() in options.nth(i).inner_text().lower():
                    options.nth(i).click()
                    break

        self.page.wait_for_timeout(800)

    # ---------- reCAPTCHA ----------
    def click_recaptcha_checkbox(self):
        frame = self.page.frame_locator(self.RecaptchaFrame)
        frame.locator(self.RecaptchaCheckbox).click(force=True)
        self.page.wait_for_timeout(1000)

    def wait_for_recaptcha_solved(self, timeout=120):
        try:
            self.page.wait_for_function(
                """
                () => {
                    const el = document.getElementById('g-recaptcha-response');
                    return el && el.value.length > 0;
                }
                """,
                timeout=timeout * 1000
            )
        except PlaywrightTimeoutError:
            raise PlaywrightTimeoutError(
                f"reCAPTCHA not solved within {timeout} seconds"
            )

    # ---------- SIGNUP FLOW ----------
    def signup(self, captcha_timeout=120):
        # Step 1
        self.page.fill(self.Firstname, config.Firstname)
        self.page.wait_for_timeout(800)

        self.page.fill(self.Lastname, config.Lastname)
        self.page.wait_for_timeout(800)

        self.page.fill(self.Username, config.Username)
        self.page.wait_for_timeout(800)

        self.select_dropdown_by_text(self.WhatIndustry, config.WhatIndustry)
        self.select_dropdown_by_text(self.SpecifyIndustry, config.SpecifyIndustry)

        self.page.fill(self.CompanyName, config.CompanyName)
        self.page.wait_for_timeout(800)

        self.select_dropdown_by_text(self.SelectCountry, config.SelectCountry)
        self.select_dropdown_by_text(self.Selectjobtitle, config.Selectjobtitle)

        self.page.fill(self.PhoneNumber, config.PhoneNumber)
        self.page.wait_for_timeout(800)

        self.page.fill(self.Email, config.Email)
        self.page.wait_for_timeout(800)

        self.page.click(self.NextBtn)
        self.page.wait_for_timeout(1500)

        # Step 2
        self.page.fill(self.CompanyAddress, config.CompanyAddress)
        self.page.wait_for_timeout(800)

        self.page.fill(self.City, config.City)
        self.page.wait_for_timeout(800)

        self.page.fill(self.State, config.State)
        self.page.wait_for_timeout(800)

        self.page.fill(self.Zipcode, config.Zipcode)
        self.page.wait_for_timeout(800)

        self.page.check(self.Term_and_Conditions)
        self.page.wait_for_timeout(1000)

        # reCAPTCHA
        self.click_recaptcha_checkbox()
        self.wait_for_recaptcha_solved(captcha_timeout)

        # Submit
        self.page.click(self.CreateAccountBtn)
        self.page.wait_for_timeout(2000)
