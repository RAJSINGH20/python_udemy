from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock : bool = True


product1 = Product(id=1,name="laptop",price = 9999.99,in_stock=True)
product2 = Product(id=2,name="smartphone",price =777.77)
product3 = Product(id=3,name="keybord",price =1789.77)

print(product1)
print(product2)
print(product3)