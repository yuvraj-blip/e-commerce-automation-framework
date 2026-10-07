from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver(headless: bool = False):
    """
    Initializes and configures the Chrome WebDriver instance.
    Supports both headed and headless execution modes.
    """
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    return driver
