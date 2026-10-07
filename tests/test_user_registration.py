import json
import time
from pathlib import Path
import pytest
from Pages.home_page import HomePage
from Pages.signup_page import SignUp
from Pages.enter_acct_info_page import EnterAccountInfo
from Pages.acct_created_page import AccountCreated
from Pages.nav_bar import NavBar
from Pages.account_delete_page import AccountDelete

def load_test_data():
    file_path = Path(__file__).resolve().parent.parent / "test_data" / "user_data.json"
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.parametrize("user_data", load_test_data())
def test_register_user_and_delete_account(driver, user_data):
    """
    Test Case 1: Register User and Delete Account
    Workflow:
      1. Launch browser & navigate to 'https://automationexercise.com/'
      2. Verify home page is visible successfully
      3. Click on 'Signup / Login' button
      4. Verify 'New User Signup!' is visible
      5. Enter name and email address and click 'Signup'
      6. Verify that 'ENTER ACCOUNT INFORMATION' is visible
      7. Fill details: Title, Name, Email, Password, Date of birth
      8. Select checkboxes for newsletter and special offers
      9. Fill address information: First name, Last name, Company, Address, etc.
      10. Click 'Create Account' button
      11. Verify that 'ACCOUNT CREATED!' is visible
      12. Click 'Continue' button
      13. Verify that 'Logged in as username' is visible
      14. Click 'Delete Account' button
      15. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    """
    # 1. Initialize Page Objects
    home_page = HomePage(driver)
    sign_up = SignUp(driver)
    enter_account_info = EnterAccountInfo(driver)
    account_created = AccountCreated(driver)
    nav_bar = NavBar(driver)
    account_deleted = AccountDelete(driver)

    # Generate a unique timestamped email to guarantee test repeatability
    timestamp = int(time.time())
    unique_email = f"tester_{timestamp}@example.com"
    user_name = user_data["name"]

    # 2. Open Home Page & Verify Title
    home_page.open()
    assert "Automation Exercise" in driver.title, "Home page title verification failed."

    # 3. Click 'Signup / Login'
    home_page.click_signup_or_login()

    # 4. Verify 'New User Signup!' is visible
    assert sign_up.is_new_user_signup_visible(), "'New User Signup!' section is not visible."

    # 5. Enter name and email address and click 'Signup' button
    sign_up.signup_details(user_name, unique_email)

    # 6. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert enter_account_info.is_account_info_visible(), "'ENTER ACCOUNT INFORMATION' header is not visible."

    # 7. Fill details: Title, Password, Date of birth
    enter_account_info.select_title(user_data["title"])
    enter_account_info.enter_password(user_data["password"])
    enter_account_info.select_dob(**user_data["dob"])

    # 8. Select checkboxes: 'Sign up for our newsletter!' and 'Receive special offers'
    if user_data.get("newsletter", False):
        enter_account_info.select_newsletter()

    if user_data.get("special_offers", False):
        enter_account_info.select_offers()

    # 9. Fill address details
    enter_account_info.address_fill(**user_data["address_info"])

    # 10. Click 'Create Account' button
    enter_account_info.click_create_account()

    # 11. Verify that 'ACCOUNT CREATED!' is visible
    assert account_created.verify_account_created(), "Expected 'ACCOUNT CREATED!' page was not visible."

    # 12. Click 'Continue' button
    account_created.click_continue()

    # 13. Verify that 'Logged in as username' is visible
    assert nav_bar.verify_logged_in(user_name), f"User '{user_name}' is not displayed as logged in."

    # 14. Click 'Delete Account' button
    nav_bar.click_delete_account()

    # 15. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    assert account_deleted.verify_text(), "'ACCOUNT DELETED!' confirmation was not visible."
    account_deleted.continue_button()
