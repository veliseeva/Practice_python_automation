from selene import browser, have, command, by
from selene.support.shared.jquery_style import s, ss
from demoqa_tests import resource


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        s('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        s('#lastName').type(value)
        return self

    def fill_email(self, value):
        s('#userEmail').type(value)
        return self

    def fill_gender(self, value):
        s(f'[name=gender][value={value}]+label').click()
        return self

    def fill_mobile_number(self, value):
        s('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__year-select').click()
        s('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        s('.react-datepicker__month-select').click()
        s('.react-datepicker__month-select').element(f'[value="{month}"]').click()
        s(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subject(self, value):
        s('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobby(self, *values):
        for value in values:
            ss('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, value):
        s('#uploadPicture').send_keys(resource.path(value))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, value):
        s('#state').click()
        s(by.text(value)).click()
        return self

    def fill_city(self, value):
        s('#city').click()
        s(by.text(value)).click()
        return self

    def submit_form(self):
        s('#submit').perform(command.js.click)
        return self

    def should_have_modal_with(self, title):
        browser.element('.modal-header').perform(command.js.scroll_into_view).should(have.exact_text(title))
        return self

    def should_have_registered_user_with(self, full_name, email, gender, mobile_number, date_of_birth,
                                         subjects, hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )
        return self
