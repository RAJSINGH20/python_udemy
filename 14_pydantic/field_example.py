from pydantic import BaseModel
from typing import List, Dict, Optional


# Cart model
class Cart(BaseModel):
    userid: int
    items: List[str]
    quantities: Dict[str, int]


# Blog post model
class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


# Cart data
cart_data = {
    "userid": 123,
    "items": [
        "Masala Chai",
        "Ginger Chai"
    ],
    "quantities": {
        "Masala Chai": 2,
        "Ginger Chai": 1
    }
}

# Create Cart object
cart = Cart(**cart_data)
print(cart)

print("-" * 40)

# Blog post data
blog_data = {
    "title": "Benefits of Masala Chai",
    "content": "Masala chai is one of the most popular beverages in India.",
    "image_url": "https://example.com/chai.jpg"
}

# Create BlogPost object
blog = BlogPost(**blog_data)
print(blog)