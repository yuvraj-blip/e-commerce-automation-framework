from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class AccountDelete(BasePage):
    """
    Page Object representing the 'Account Deleted' confirmation page.
    """
    DELETE_TEXT = (By.CSS_SELECTOR, "h2[data-qa='account-deleted']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def verify_text(self) -> bool:
        return self.is_visible(self.DELETE_TEXT)

    def continue_button(self):
        self.click(self.CONTINUE_BUTTON)
