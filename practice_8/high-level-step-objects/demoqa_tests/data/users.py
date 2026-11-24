from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import List


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    maths = 'Maths'
    english = 'English'
    hindi = 'Hindi'


class DateOfBirth:
    def __init__(self, value_entered):
        self.value_entered = value_entered
        self.raw_date = datetime.strptime(value_entered, '%d %b %Y')
        self.value_in_modal = datetime.strftime(self.raw_date, '%d %B,%Y')
        self.day_formatted = self.raw_date.strftime('%d')
        self.month_formatted = self.raw_date.strftime('%B')


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    date_of_birth: DateOfBirth
    subjects: List[Subject]
    hobbies: List[Hobby]
    picture: str
    current_address: str
    state: str
    city: str
