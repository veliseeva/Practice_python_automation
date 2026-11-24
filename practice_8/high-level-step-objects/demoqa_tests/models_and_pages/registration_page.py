from demoqa_tests.data.users import User
from selene import browser, have, command
from selene.support.shared.jquery_style import s, ss

from demoqa_tests import resource

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def register(self, user: User):
        s('#firstName').type(user.first_name)
        s('#lastName').type(user.last_name)
        s('#userEmail').type(user.email)
        ss('#genterWrapper .custom-control').element_by(have.exact_text(user.gender.value)).click()
        s('#userNumber').type(user.mobile_number)

        s('#dateOfBirthInput').click()
        s('.react-datepicker__year-select').send_keys(user.date_of_birth.raw_date.year).click()
        s('.react-datepicker__month-select').send_keys(user.date_of_birth.month_formatted).click()
        s(f'.react-datepicker__day--0{user.date_of_birth.day_formatted}:not(.react-datepicker__day--outside-month)').click()

        for subject in user.subjects:
            s('#subjectsInput').type(subject.value).press_enter()

        for hobby in user.hobbies:
            ss('[for^=hobbies-checkbox]').element_by(have.exact_text(hobby.value)).click()

        s('#currentAddress').type(user.current_address)
        s('#uploadPicture').send_keys(resource.path(user.picture))

        s('#state').perform(command.js.scroll_into_view).click()
        ss('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()

        s('#city').perform(command.js.scroll_into_view).click()
        ss('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()

        s('#submit').perform(command.js.click)
        return self

    def should_have_registered(self, user: User):
        s('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender.value,
                user.mobile_number,
                user.date_of_birth.value_in_modal,
                f'{", ".join([subject.value for subject in user.subjects])}',
                f'{", ".join([hobby.value for hobby in user.hobbies])}',
                user.picture,
                user.current_address,
                f'{user.state} {user.city}'
            )
        )