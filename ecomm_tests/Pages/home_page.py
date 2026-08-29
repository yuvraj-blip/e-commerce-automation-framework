from selenium.webdriver.common.by import By
from ecomm_tests.Pages.base_page import BasePage

class HomePage(BasePage):

    signup_or_login = (By.CSS_SELECTOR,"a[href='/login']")

    def click_signup_or_login(self):
        self.click(self.signup_or_login)

