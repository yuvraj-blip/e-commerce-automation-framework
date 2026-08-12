
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:

    USERNAME_LOGIN = (By.ID,"username")
    PASSWORD_LOGIN = (By.ID,"password")
    BUTTON_LOGIN = (By.ID,"submit")


    def __init__(self,driver,base_url):
        self.driver = driver
        self.base_url = base_url

    def login(self,username,password):
        self.driver.get(self.base_url)
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.USERNAME_LOGIN)).send_keys(username)
       
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.PASSWORD_LOGIN)).send_keys(password)
      
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.BUTTON_LOGIN)).click()
        

    

