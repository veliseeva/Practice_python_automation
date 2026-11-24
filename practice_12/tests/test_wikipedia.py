import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_android_search(mobile):
    if mobile == "ios":
        pytest.skip("Test android")
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

    with step('Click link'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.first.click()

def test_ios_search(mobile):
        if mobile == "android":
            pytest.skip("Test ios")
        with step("Input text"):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type("Python\n")
        with step("Verify content found"):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("Python"))