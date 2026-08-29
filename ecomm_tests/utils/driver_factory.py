from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver(headless: bool = False):

    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    driver = webdriver.chrome(options=options)
    return driver
