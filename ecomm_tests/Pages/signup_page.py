from selenium.webdriver.common.by import By
from ecomm_tests.Pages.base_page import BasePage

class SignUp(BasePage):

    verify_page = (By.XPATH,"//h2[text()='New User Signup!']")
    signup_name_input = (By.CSS_SELECTOR,"input[data-qa='data-qa']")
    signup_email_input = (By.CSS_SELECTOR,"input[data-qa='signup-email']")
    signup_button = (By.CSS_SELECTOR,"button[data-qa='signup-button']")

    def is_new_user_signup_visible(self):
        return self.is_visible(self.verify_page)
    
    def signup_details(self,name,email):
        self.enter_text(self.signup_name_input,name)
        self.enter_text(self.signup_email_input,email)
        self.click(self.signup_button)





