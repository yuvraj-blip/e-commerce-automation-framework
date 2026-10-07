from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class AccountCreated(BasePage):
    """
    Page Object representing the 'Account Created' confirmation page.
    """
    ACCT_CREATED = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def verify_account_created(self) -> bool:
        return self.is_visible(self.ACCT_CREATED)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

accountCreate = AccountCreated
