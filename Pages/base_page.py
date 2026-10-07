from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    """
    BasePage encapsulates common Selenium WebDriver interactions,
    providing reliable explicit waits and synchronization methods.
    """
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(str(text))

    def get_text(self, locator) -> str:
        return self.find_visible(locator).text

    def select_dropdown_value(self, locator, value):
        dropdown = Select(self.find_visible(locator))
        dropdown.select_by_value(str(value))

    def is_visible(self, locator) -> bool:
        try:
            return self.find_visible(locator).is_displayed()
        except Exception:
            return False
