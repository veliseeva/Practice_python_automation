from demoqa_tests.models_and_pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User, Gender, Hobby, Subject, DateOfBirth
import datetime

user1 = User(
    first_name='Ivan',
    last_name='Ivanov',
    email='sobaka@mail.ru',
    mobile_number='8999444567',
    gender=Gender.male,
    date_of_birth=DateOfBirth('08 Aug 1991'),  # Год, месяц, день
    subjects=[Subject.maths],  # Список!
    hobbies=[Hobby.sports, Hobby.reading],
    picture='picture.jpg',
    current_address='u. Lenina, d. 15, kv. 16',
    state='NCR',
    city='Delhi'
)


def test_high_level_registration():
    registration_page = RegistrationPage()

    (registration_page
     .open()
     .register(user1)
     .should_have_registered(user1)
     )
