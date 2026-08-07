from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, List, Union


# Address model
class Address(BaseModel):
    street: str
    city: str
    postal_code: str


# Company model
class Company(BaseModel):
    name: str
    address: Optional[Address] = None


# Employee model
class Employee(BaseModel):
    name: str
    company: Optional[Company] = None


# Text content model
class TextContent(BaseModel):
    type: str = "text"
    content: str


# Image content model
class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str


# Article model
class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]


# Country model
class Country(BaseModel):
    name: str
    code: str


# State model
class State(BaseModel):
    name: str
    country: Country


# City model
class City(BaseModel):
    name: str
    state: State


# Organization address model
class OrganizationAddress(BaseModel):
    street: str
    city: City
    postal_code: str


# Organization model
class Organization(BaseModel):
    name: str
    headquarters: OrganizationAddress
    branches: List[OrganizationAddress]


# -------------------------
# Sample Data
# -------------------------

company = Company(
    name="OpenAI",
    address=Address(
        street="123 AI Street",
        city="San Francisco",
        postal_code="94105"
    )
)

employee = Employee(
    name="Raj Singh",
    company=company
)

article = Article(
    title="Introduction to AI",
    sections=[
        TextContent(
            content="Artificial Intelligence is transforming the world."
        ),
        ImageContent(
            url="https://example.com/ai.jpg",
            alt_text="AI Illustration"
        )
    ]
)

country = Country(
    name="India",
    code="IN"
)

state = State(
    name="West Bengal",
    country=country
)

city = City(
    name="Durgapur",
    state=state
)

headquarters = OrganizationAddress(
    street="Main Office Road",
    city=city,
    postal_code="713201"
)

branch = OrganizationAddress(
    street="Branch Office Road",
    city=city,
    postal_code="713202"
)

organization = Organization(
    name="Tech Solutions",
    headquarters=headquarters,
    branches=[branch]
)

print("\nCompany")
print(company.model_dump_json(indent=4))

print("\nEmployee")
print(employee.model_dump_json(indent=4))

print("\nArticle")
print(article.model_dump_json(indent=4))

print("\nOrganization")
print(organization.model_dump_json(indent=4))