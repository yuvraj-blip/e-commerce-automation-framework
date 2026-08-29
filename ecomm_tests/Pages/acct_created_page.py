from selenium.webdriver.common.by import By
from ecomm_tests.Pages.base_page import BasePage

class accountCreate(BasePage):

    ACCT_CREATED = (By.CSS_SELECTOR,"h2[data-qa='account-created']")
    CONTINUE = (By.CSS_SELECTOR,"a[data-qa = 'continue-button']")

    def verify_account_created(self):
        return self.is_visible(self.ACCT_CREATED)

    def click_continue(self):
        self.click(self.CONTINUE)
        