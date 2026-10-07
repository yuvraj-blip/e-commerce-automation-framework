from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class HomePage(BasePage):
    """
    Page Object representing the Automation Exercise Home Page.
    """
    URL = "https://automationexercise.com/"
    SIGNUP_OR_LOGIN = (By.CSS_SELECTOR, "a[href='/login']")

    def open(self):
        self.driver.get(self.URL)

    def click_signup_or_login(self):
        self.click(self.SIGNUP_OR_LOGIN)
