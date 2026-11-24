from selene import browser

from demoqa_test.models.components.panel import Panel
from demoqa_test.models.pages.simplified_reg_form_page import SimplifiedRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simplified_reg_form = SimplifiedRegistrationPage()
        self.left_panel = Panel()

    def open(self):
        browser.open('/')
        return self
