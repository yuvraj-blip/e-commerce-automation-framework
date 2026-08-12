import os 
import json
import pytest
from dotenv import load_dotenv
from Pages.login import Login
from Pages.logout import Logout

def load_test_data():
    with open ("test_data/credentials.json","r") as file:
        return json.load(file)


@pytest.mark.login
@pytest.mark.parametrize("user_data",load_test_data())

def test_valid_login(driver,user_data):   
    load_dotenv()
    base_url = os.getenv("base_url")
    login_page = Login(driver,base_url)
    logout_page = Logout(driver)

    login_page.login(user_data["username"],user_data['password'])
    assert "practicetestautomation.com/logged-in-successfully/" in driver.current_url 

    text = logout_page.verify_login()
    assert 'Congratulations' in text or 'successfully logged in' in text

    logout_page.logout()

    



    

    



