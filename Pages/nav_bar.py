from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class NavBar(BasePage):
    """
    Page Object representing the Top Navigation Bar.
    """
    LOGGED_IN_VERIFY = (By.XPATH, "//a[i[contains(@class, 'fa-user')]]")
    DELETE_BUTTON = (By.CSS_SELECTOR, "a[href='/delete_account']")

    def get_logged_in_text(self) -> str:
        return self.get_text(self.LOGGED_IN_VERIFY)

    def verify_logged_in(self, username: str = None) -> bool:
        full_text = self.get_logged_in_text()
        if "Logged in as" not in full_text:
            return False
        if username:
            return username in full_text
        return True

    def click_delete_account(self):
        self.click(self.DELETE_BUTTON)
