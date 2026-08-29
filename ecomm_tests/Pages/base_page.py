from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self,driver,timeout=15):
        self.driver = driver
        self.timeout = timeout

    def find(self,locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
    
    def click(self,locator):
        element= WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        
    def enter_text(self,locator,text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)   

    def get_text(self,locator):
        return self.find(locator).text

    def select_dropdown_value(self,locator,value):
        dropdown = Select(self.find(locator))
        dropdown.select_by_value(value)
    
    def is_visible(self,locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False
    