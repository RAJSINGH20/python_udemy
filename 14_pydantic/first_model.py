from pydantic import BaseModel

class User(BaseModel):
    id: int 
    name: str
    is_Active: bool

input_data = {"id":101,"name":"chai code","is_Active":True}
user = User(**input_data)

print(user)