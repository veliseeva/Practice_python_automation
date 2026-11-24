
from selene import browser, by


def test_desktop_fixture(desktop_browser):
    browser.open("https://github.com/")
    browser.element(by.text("Sign up")).click()


def test_mobile_fixture(mobile_browser):
    browser.open("https://github.com/")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()
