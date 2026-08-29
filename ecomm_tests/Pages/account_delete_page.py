from selenium.webdriver.common.by import By
from ecomm_tests.Pages.base_page import BasePage

class AccountDelete(BasePage):

    DELETE_TEXT = (By.CSS_SELECTOR,"h2[data-qa = 'account-deleted']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR,"a[data-qa = 'continue-button']")

    def verify_text(self):
        return self.is_visible(self.DELETE_TEXT)
    
    def continue_button(self):
        return self.click(self.CONTINUE_BUTTON)
    
    