from datetime import date
from pydantic import BaseModel, ValidationError, field_validator

class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

@field_validator("birthdate")
def valid_birthdate(cls, v: date):
    delta = date.today() - v
    age = delta.days / 365
    if age > 120:
        raise ValueError("You seem a bit too old!")
    return v


try:
    person = Person(
    first_name="str",
    last_name= "str",
    birthdate= "1500-05-01")
    print(person)
except ValidationError as e:
    print(e)

