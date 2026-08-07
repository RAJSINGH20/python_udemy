from pydantic import BaseModel , computed_field ,Field

class Product(BaseModel):
    price: float
    quantity: int
    
    @computed_field
    @property
    def total_price(self)-> float:
        return self.price * self.quantity

class Booking(BaseModel):
    userId: int
    roomId: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_price(self) -> float:
        return self.nights * self.rate_per_night

product = Product(
    price=250.0,
    quantity=3
)
print(product)
print(product.total_price)


booking= Booking(
    userId=123,
    roomId=456,
    nights=4,
    rate_per_night=1500.0
    
)
print(booking)
print(booking.total_price)
print(booking.model_dump())