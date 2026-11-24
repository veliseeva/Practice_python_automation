import os
from selene import have, be, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_fill_the_form():
    browser.open('/')

    browser.execute_script('document.querySelector("footer").remove()')
    browser.execute_script('document.getElementById("fixedban").remove()')

    s('#firstName').type('Ivan')
    s('#lastName').type('Ivanov')
    s('#userEmail').type('sobaka@mail.ru')

    s('[for="gender-radio-1"]').click()
    s('#userNumber').type('8999444567')

    s('#dateOfBirthInput').click()
    s('.react-datepicker__year-select').click()
    s('.react-datepicker__year-select').element('[value="2009"]').click()
    s('.react-datepicker__month-select').click()
    s('.react-datepicker__month-select').element('[value="9"]').click()  # 9 - это Октябрь
    s('.react-datepicker__day--010').click()

    s('#subjectsInput').type("Maths").press_enter()


    s('[for="hobbies-checkbox-1"]').click()
    s('[for="hobbies-checkbox-3"]').click()

    path_to_file = os.path.join(os.path.dirname(__file__),
                                'picture.jpg')
    s('#uploadPicture').send_keys(path_to_file)

    s('#currentAddress').type('u. Lenina, d. 15, kv. 16')
    s('#state').click()
    s(by.text("NCR")).click()
    s('#city').click()
    s(by.text('Delhi')).click()

    s('#submit').execute_script('element.click()')

    s('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    results_table = s('.table-responsive')
    results_table.should(have.text('Ivan Ivanov'))
    results_table.should(have.text('sobaka@mail.ru'))
    results_table.should(have.text('Male'))
    results_table.should(have.text('8999444567'))
    results_table.should(have.text('10 October,2009'))
    results_table.should(have.text('Maths'))
    results_table.should(have.text('Sports, Music'))
    results_table.should(have.text('picture.jpg'))
    results_table.should(have.text('Moscow, u. Lenina, d. 15, kv. 16'))
    results_table.should(have.text('NCR Delhi'))

