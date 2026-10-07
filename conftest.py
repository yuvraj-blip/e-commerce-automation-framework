import pytest
from utils.driver_factory import create_driver

def pytest_addoption(parser):
    """
    Registers custom command-line options for pytest.
    """
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser tests in headless mode"
    )

@pytest.fixture
def driver(request):
    """
    Pytest fixture to initialize and quit the WebDriver per test.
    Supports '--headless' CLI flag for CI/CD environments.
    """
    is_headless = request.config.getoption("--headless")
    drv = create_driver(headless=is_headless)
    yield drv
    drv.quit()
