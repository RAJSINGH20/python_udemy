from pydantic import BaseModel, field_validator, model_validator


# User model
class User(BaseModel):
    username: str

    # Validate username length
    @field_validator("username")
    @classmethod
    def username_length(cls, value):
        if len(value) < 4:
            raise ValueError("Username must be at least 4 characters long.")
        return value


# Signup model
class SignupData(BaseModel):
    password: str
    confirm_password: str

    # Validate that both passwords match
    @model_validator(mode="after")
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match.")
        return self


# Test User model
user = User(username="RajSingh")
print(user)

# Test SignupData model
signup = SignupData(
    password="mypassword123",
    confirm_password="mypassword123"
)
print(signup)