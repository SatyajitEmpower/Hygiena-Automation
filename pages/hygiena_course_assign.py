import re
from playwright.sync_api import Page
from datetime import datetime
from playwright.sync_api import expect
from pages.base_page import BasePage
import time
from config.config import config

class CourseAssign(BasePage):
    """Playwright Page Object for course purchase + user assignment (DevExtreme)."""

    # ---------- LOCATORS ----------
    ELearning_btn = "#elearningSpan"
    Course_btn = "#tab-courses"

    # ---------- COURSE SELECTION ----------
    # FHT_Checkbox = '#course-card-food_handler_training input[type="checkbox"]'
    # FMT_Checkbox = '#course-card-food_manager_training input[type="checkbox"]'
    # Select_FHT_Course = '#course-card-food_handler_training'
    # Select_FMT_Course = '#course-card-food_manager_training'
    
    # ---------- Select Course Quantity (input + spinner fallbacks) ----------
    # Prefer input selectors; fallbacks will be tried in code if these are not present
    FHT_Course_quantity = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/dx-number-box/div/div[2]/div[2]/div[1]"
    FMT_Course_quantity = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/dx-number-box/div/div[2]/div[2]/div[1]/div"
    Buy_now_btn = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div[3]/button"
    Complete_purchase_btn = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div[3]/button/span"

    Assign_FHT_user = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/dx-select-box/div[1]/div/div[1]/input"
    Assign_FMT_user = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/dx-select-box/div[1]/div/div[1]/input"

    Due_date_FHT = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]//input"
    Due_date_FMT = "xpath=//*[@id='homeView']/div/app-empower/div/div/div[2]/div[2]/table/tbody/tr[2]/td[3]//input"
    Card_number_input = "#cardNumber"
    Expiry_date_input = "#cardExpiry"
    CVC_input = "#cardCvc"
    Card_holder_name_input = "#billingName"
    Country_name_input = "#billingCountry"
    Zip_code_input = "#billingPostalCode"
    Pay_btn = "xpath=//*[@id='payment-form']/div/div/div/div[3]/div/div[2]/div/button"

    DX_POPUP_ITEMS = ".dx-overlay-wrapper .dx-list-item"

    def __init__(self, page: Page):
        super().__init__(page)

    # ---------- HELPERS ----------
    def select_user_by_course(self, locator, text):
        time.sleep(1)
        dropdown = self.page.locator(locator)
        dropdown.select_option(label=text)
        time.sleep(1)
        

    # ---------- NAVIGATION ----------
    def click_elearning(self):
        self.page.locator(self.ELearning_btn).click()
        self.wait_for_network()
        self.page.wait_for_timeout(500)

    def click_course_tab(self):
        self.page.locator(self.Course_btn).click()
        self.wait_for_network()
        self.page.wait_for_timeout(300)

    # def _check_course(self, checkbox_selector: str, card_selector: str | None = None):
    #     """Ensure the course checkbox ends up checked; try click → card click → JS fallback."""
    #     checkbox = self.page.locator(checkbox_selector).first
    #     checkbox.wait_for(state="attached", timeout=15000)
    #     checkbox.scroll_into_view_if_needed()

    #     # 1) Try native check
    #     try:
    #         checkbox.check(force=True)
    #     except Exception:
    #         pass

    #     # 2) If still not checked, try clicking the card container
    #     try:
    #         if not checkbox.is_checked():
    #             if card_selector:
    #                 self.page.locator(card_selector).click(force=True)
    #     except Exception:
    #         pass

    #     # 3) If still not checked, set via JS to trigger change events
    #     if not checkbox.is_checked():
    #         self.page.evaluate(
    #             """
    #             (selector) => {
    #                 const el = document.querySelector(selector);
    #                 if (!el) throw 'Checkbox not found';
    #                 el.checked = true;
    #                 el.dispatchEvent(new Event('input', { bubbles: true }));
    #                 el.dispatchEvent(new Event('change', { bubbles: true }));
    #                 el.dispatchEvent(new Event('click', { bubbles: true }));
    #             }
    #             """,
    #             checkbox_selector,
    #         )

    #     expect(checkbox).to_be_checked()

    # def _ensure_checked_by_xpath(self, checkbox_xpath: str, card_xpath: str = None):
    #     cb = self.page.locator(checkbox_xpath).first
    #     cb.wait_for(state="attached", timeout=1000)
    #     cb.scroll_into_view_if_needed()

    #     # Use JavaScript to check the checkbox and trigger events
    #     self.page.evaluate(
    #         """
    #         ({ selector }) => {
    #             const el = document.querySelector(selector);
    #             if (!el) throw 'Checkbox not found';
                
    #             el.checked = true;
    #             el.dispatchEvent(new Event('change', { bubbles: true }));
    #             el.dispatchEvent(new Event('click', { bubbles: true }));
    #         }
    #         """,
    #         {"selector": checkbox_xpath},
    #     )
        
    #     self.page.wait_for_timeout(5000)
        
    #     # Verify checkbox is checked
    #     expect(cb).to_be_checked()

    #     # Optional: if UI uses "selected" class on card, assert it too
    #     if card_xpath:
    #         card = self.page.locator(card_xpath).first
    #         expect(card).to_have_class(re.compile(r".*\bselected\b.*"))

    # def select_both_courses(self):
    #     self._check_course(self.FHT_Checkbox, self.Select_FHT_Course)
    #     self.page.wait_for_timeout(500)

    #     self._check_course(self.FMT_Checkbox, self.Select_FMT_Course)
    #     self.page.wait_for_timeout(500)

    # def select_fht_course_quantity(self, quantity):
    #     self._set_quantity(self.FHT_Course_quantity, quantity)

    # def select_fmt_course_quantity(self, quantity):
    #     self._set_quantity(self.FMT_Course_quantity, quantity)
 
    # def _set_quantity(self, input_selector, quantity):
    #     qty = str(int(quantity))

    #     # Wait until quantity input is rendered AFTER Buy Now
    #     self.page.wait_for_selector(input_selector, timeout=15000)

    #     # 🔥 XPath-safe JS execution
    #     self.page.evaluate(
    #         """
    #         ({ xpath, value }) => {
    #             const el = document
    #                 .evaluate(xpath.replace('xpath=', ''), document, null,
    #                         XPathResult.FIRST_ORDERED_NODE_TYPE, null)
    #                 .singleNodeValue;

    #             if (!el) throw 'Quantity input not found';

    #             el.removeAttribute('readonly');
    #             el.value = value;

    #             el.dispatchEvent(new Event('input', { bubbles: true }));
    #             el.dispatchEvent(new Event('change', { bubbles: true }));
    #         }
    #         """,
    #         {"xpath": input_selector, "value": qty},
    #     )

    #     self.page.wait_for_timeout(500)

    # def click_buy_now(self):
    #     locator = self.page.locator(self.Buy_now_btn)
    #     try:
    #         locator.click()
    #     except Exception:
    #         # If button is present but disabled, try enabling via JS then force click
    #         try:
    #             self.page.eval_on_selector(self.Buy_now_btn, "el => { el.removeAttribute('disabled'); el.classList.remove('disabled'); }")
    #             locator.click(force=True)
    #         except Exception:
    #             # fallback: force click directly
    #             locator.click(force=True)
    #     self.wait_for_network()
    #     self.page.wait_for_timeout(5000)

    def click_fht_course_quantity(self):
        self.page.locator(self.FHT_Course_quantity).click()
        self.wait_for_network()
        self.page.wait_for_timeout(300)

    def click_fmt_course_quantity(self):
        self.page.locator(self.FMT_Course_quantity).click()
        self.wait_for_network()
        self.page.wait_for_timeout(300)

    def click_buy_now(self):
        self.page.locator(self.Buy_now_btn).click()
        self.wait_for_network()
        self.page.wait_for_timeout(500)

    # Role
    # def assign_users_to_courses(self):
    #     self.select_user_by_course(self.Assign_FHT_user, "John Doe")
    #     self.page.wait_for_timeout(500)
    # def assign_fmt_user(self):
    #     self.select_user_by_course(self.Assign_FMT_user, "John Doe")
    #     self.page.wait_for_timeout(500)

    def click_complete_purchase(self):
        self.page.locator(self.Complete_purchase_btn).click()
        self.wait_for_network()
        self.page.wait_for_timeout(500)

    # ---------- CARD DETAILS ----------
    def enter_card_details(self):
        self.page.fill(self.Card_number_input, config.Card_number)
        self.page.fill(self.Expiry_date_input, config.Expiry_date)
        self.page.fill(self.CVC_input, config.CVC)
        self.page.fill(self.Card_holder_name_input, config.Card_holder_name)
        self.page.select_option(self.Country_name_input, label=config.Country_name)
        self.page.fill(self.Zip_code_input, config.Zip_code)
        self.page.wait_for_timeout(5000)
        Pay_button=self.page.locator(self.Pay_btn)
        Pay_button.click()
        self.page.wait_for_timeout(5000)
    # ---------- ASSIGN USERS (DevExtreme) ----------
    def assign_fht_user(self, username):
        self._select_dx_user(self.Assign_FHT_user, username)

    def assign_fmt_user(self, username):
        self._select_dx_user(self.Assign_FMT_user, username)

    def _select_dx_user(self, input_selector, text):
        inp = self.page.locator(input_selector)
        inp.click()
        # Try to type into the input; if it's readonly this may fail, so ignore errors
        try:
            inp.fill(text, timeout=1000)
        except Exception:
            pass

        # Ensure the dropdown opens; pressing ArrowDown often opens DevExtreme listboxes
        try:
            inp.press("ArrowDown")
        except Exception:
            pass

        items = self.page.locator(self.DX_POPUP_ITEMS)
        # wait for at least one item to appear
        try:
            items.first.wait_for(timeout=5000)
        except Exception:
            raise Exception(f"Dropdown items not found for selector: {input_selector}")

        count = items.count()
        for i in range(count):
            label = items.nth(i).inner_text().strip()
            if label.lower() == text.lower():
                items.nth(i).click()
                break
        else:
            raise Exception(f"User '{text}' not found in dropdown")

        # Close overlay
        self.page.keyboard.press("Escape")

    # ---------- DUE DATE ----------
    def _normalize_date(self, date_str):
        for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"):
            try:
                dt = datetime.strptime(date_str.strip(), fmt)
                return dt.strftime("%Y-%m-%d"), dt.strftime("%m/%d/%Y")
            except ValueError:
                continue
        raise ValueError(f"Unsupported date format: {date_str}")

    def set_due_date(self, selector, date_str):
        yyyy_mm_dd, mm_dd_yyyy = self._normalize_date(date_str)

        el = self.page.locator(selector)
        el.scroll_into_view_if_needed()

        input_type = el.get_attribute("type") or ""

        if input_type == "date":
            # Use eval_on_selector to run script on the matched element
            self.page.eval_on_selector(
                selector,
                "(el, val) => { el.value = val; el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }",
                yyyy_mm_dd,
            )
        else:
            el.fill(mm_dd_yyyy)
            self.page.keyboard.press("Tab")

    def set_due_date_fht(self, date):
        self.set_due_date(self.Due_date_FHT, date)

    def set_due_date_fmt(self, date):
        self.set_due_date(self.Due_date_FMT, date)




