from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Logout:
    
    VERIFY_LOGIN = (By.CSS_SELECTOR,"p.wp-block-paragraph strong")
    LOGOUT = (By.CSS_SELECTOR,"a.wp-block-button__link")

    def __init__(self,driver):
        self.driver = driver
        
    def verify_login(self): 
        text = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.VERIFY_LOGIN)).text
        return text
    def logout(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.LOGOUT)).click()
    