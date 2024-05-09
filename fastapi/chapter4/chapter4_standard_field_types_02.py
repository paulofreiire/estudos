from datetime import date
from enum import Enum
from typing import List
from pydantic import BaseModel, ValidationError

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]

try:
    # Valid
    person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    birthdate="1991-01-01",
    interests=["travel", "sports"],
    )
    # first_name='John' last_name='Doe' gender=<Gender.MALE: 'MALE'> birthdate=datetime.date(1991, 1, 1) interests=['travel', 'sports']
    print(person)      
except ValidationError as e:
    print(str(e))

