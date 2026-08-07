from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


# Person model
class Person(BaseModel):
    firstname: str
    lastname: str

    @field_validator("firstname", "lastname")
    @classmethod
    def must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError("Name must be capitalized.")
        return v


# User model
class User(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def normalize_email(cls, v):
        return v.lower().strip()


# Product model
class Product(BaseModel):
    price: float

    @field_validator("price", mode="before")
    @classmethod
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace("$", ""))
        return v


# DateRange model
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date(self):
        if self.start_date >= self.end_date:
            raise ValueError("Start date must be before end date.")
        return self


# Test Person
person = Person(
    firstname="Raj",
    lastname="Singh"
)
print(person)

# Test User
user = User(
    email="  RAJ@GMAIL.COM "
)
print(user)

# Test Product
product = Product(
    price="$499.99"
)
print(product)

# Test DateRange
date_range = DateRange(
    start_date=datetime(2026, 8, 7, 10, 0),
    end_date=datetime(2026, 8, 8, 10, 0)
)
print(date_range)