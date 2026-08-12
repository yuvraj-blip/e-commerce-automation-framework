import pytest
import selenium.webdriver 

@pytest.fixture(scope='session')
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = selenium.webdriver.Chrome()
    
    yield driver

    driver.quit()



