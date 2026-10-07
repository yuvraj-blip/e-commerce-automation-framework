from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class EnterAccountInfo(BasePage):
    """
    Page Object representing the 'Enter Account Information' form.
    """
    ACCOUNT_INFO_TITLE = (By.XPATH, "//b[text()='Enter Account Information']")
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    PASSWORD = (By.ID, "password")
    DAYS_DROPDOWN = (By.ID, "days")
    MONTH_DROPDOWN = (By.ID, "months")
    YEAR_DROPDOWN = (By.ID, "years")
    NEWSLETTER = (By.ID, "newsletter")
    OPTIN = (By.ID, "optin")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS_1 = (By.ID, "address1")
    ADDRESS_2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    def is_account_info_visible(self) -> bool:
        return self.is_visible(self.ACCOUNT_INFO_TITLE)

    def select_title(self, title: str):
        locator = self.TITLE_MR if str(title).strip().lower() in ["mr", "mr."] else self.TITLE_MRS
        self.click(locator)

    def enter_password(self, password: str):
        self.enter_text(self.PASSWORD, password)

    def select_dob(self, day, month, year):
        self.select_dropdown_value(self.DAYS_DROPDOWN, str(day))
        self.select_dropdown_value(self.MONTH_DROPDOWN, str(month))
        self.select_dropdown_value(self.YEAR_DROPDOWN, str(year))

    def select_newsletter(self):
        self.click(self.NEWSLETTER)

    def select_offers(self):
        self.click(self.OPTIN)

    def address_fill(self, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile_number):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.COMPANY, company)
        self.enter_text(self.ADDRESS_1, address1)
        self.enter_text(self.ADDRESS_2, address2)
        self.select_dropdown_value(self.COUNTRY, country)
        self.enter_text(self.STATE, state)
        self.enter_text(self.CITY, city)
        self.enter_text(self.ZIPCODE, zipcode)
        self.enter_text(self.MOBILE_NUMBER, mobile_number)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT)
