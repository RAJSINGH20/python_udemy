from typing import List , Optional
from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    postalcode:str

class User(BaseModel):
    id:int
    name:str
    address: Address

address = Address(
    street="12 Park Street",
    city="Durgapur",
    postalcode="713201"
)
print(address)

user = User(
    id=101,
    name="Raj Singh",
    address=address
)
print(user)

userData = {
    "id": 1,
    "name": "RAJ",
    "address": {
        "street": "12 Park Street",
        "city": "Durgapur",
        "postalcode": "713201"
    }
}

user = User(**userData)
print(user)