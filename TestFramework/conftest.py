import pytest
from utils.webdriver_manager import init_driver, quit_driver

@pytest.fixture(scope="class")
def setup(request):
    driver = init_driver()
    request.cls.driver = driver
    yield
    quit_driver(driver)

def pytest_html_report_title(report):
    report.title = "Automation Test Report"

def pytest_configure(config):
    config.option.htmlpath = "reports/test_report.html"
