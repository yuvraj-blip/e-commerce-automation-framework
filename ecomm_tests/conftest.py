import pytest
from utils.driver_factory import create_driver

@pytest.fixture
def driver():
    drv = create_driver
    yield drv
    drv.quit()

