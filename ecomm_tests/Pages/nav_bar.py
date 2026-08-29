from selenium.webdriver.common.by import By
from ecomm_tests.Pages.base_page import BasePage

class NavBar(BasePage):
    LOGGED_IN_VERIFY = (By.XPATH, "//a[i[contains(@class, 'fa-user')]]")
    DELETE_BUTTON = (By.CSS_SELECTOR, "a[href='/delete_account']")

    def get_logged_in_text(self):
        return self.get_text(self.LOGGED_IN_VERIFY)

    def verify_logged_in(self, expected_email):
        full_text = self.get_logged_in_text()
        return "Logged in as" in full_text and expected_email in full_text

    def click_delete_account(self):
        self.click(self.DELETE_BUTTON)