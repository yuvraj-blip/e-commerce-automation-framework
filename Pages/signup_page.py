from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class SignUp(BasePage):
    """
    Page Object representing the Signup / Login Page.
    """
    VERIFY_PAGE = (By.XPATH, "//h2[text()='New User Signup!']")
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def is_new_user_signup_visible(self) -> bool:
        return self.is_visible(self.VERIFY_PAGE)

    def signup_details(self, name: str, email: str):
        self.enter_text(self.SIGNUP_NAME_INPUT, name)
        self.enter_text(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)
