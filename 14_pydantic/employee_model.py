from typing import Optional
from pydantic import BaseModel, Field


# Employee model
class Employee(BaseModel):
    id: int

    namer: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="Employee name",
        examples=["RAJ SINGH"]
    )

    department: Optional[str] = "General"

    salary: float = Field(
        ...,
        ge=10000
    )


# Employee data
emp = {
    "id": 101,
    "namer": "Raj Singh",
    "department": "IT",
    "salary": 45000.0
}

# Create Employee object
employee = Employee(**emp)

# Print the object
print(employee)