import pytest
from selene import browser
import os
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene_base_url', 'https://demoqa.com')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 6.0
    options = Options()

    options.page_load_strategy = 'eager'

    browser.config.driver_options = options
    browser.config.driver_name = 'chrome'

    yield

    browser.quit()