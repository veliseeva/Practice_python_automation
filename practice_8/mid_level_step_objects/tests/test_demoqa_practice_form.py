from demoqa_tests.models_and_pages.registration_page import RegistrationPage


def test_new_user_all_fields_all_valid():
    # GIVEN
    registration_page = RegistrationPage()

    (registration_page.open()
      .fill_first_name('Ivan')
      .fill_last_name('Ivanov')
      .fill_email('sobaka@mail.ru')
      .fill_gender('Male')
      .fill_mobile_number('8999444567')
      .fill_date_of_birth('2009', '9', '10')
      .fill_subject('Maths')
      .fill_hobby('Sports', 'Reading')
      .upload_picture('picture.jpg')
      .fill_current_address('u. Lenina, d. 15, kv. 16')
      .fill_state('NCR')
      .fill_city('Delhi').submit_form())

    # THEN
    registration_page.should_have_modal_with('Thanks for submitting the form')
    registration_page.should_have_registered_user_with(
        'Ivan Ivanov',
        'sobaka@mail.ru',
        'Male',
        '8999444567',
        '10 October,2009',
        'Maths',
        'Sports, Reading',
        'picture.jpg',
        'u. Lenina, d. 15, kv. 16',
        'NCR Delhi')