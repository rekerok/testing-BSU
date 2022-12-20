import pytest

import utils.read_data_json
from driver.driver_singleton import Driver_Singleton


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="choose browser",
    )

    parser.addoption(
        "--environment", action="store", default="qa", help="",
    )


@pytest.fixture(autouse=True)
def driver(request):
    driver = Driver_Singleton.get_webdriver(request.config.getoption("--browser"))
    yield driver
    Driver_Singleton.quit()


@pytest.fixture
def environment(request):
    environment = request.config.getoption("--environment")
    data = utils.read_data_json.read_data_json(environment)
    return data

