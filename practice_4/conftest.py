import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function', autouse=True)

def open_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser.config.driver_options = chrome_options

    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 6
    yield
    browser.quit()