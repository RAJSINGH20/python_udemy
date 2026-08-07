from typing import List, Optional
from pydantic import BaseModel


# Recursive Comment model
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None


# Resolve forward references
Comment.model_rebuild()


# Sample data
comment_data = {
    "id": 1,
    "content": "This is the main comment.",
    "replies": [
        {
            "id": 2,
            "content": "First reply.",
            "replies": [
                {
                    "id": 3,
                    "content": "Reply to the first reply.",
                    "replies": None
                }
            ]
        },
        {
            "id": 4,
            "content": "Second reply.",
            "replies": None
        }
    ]
}

# Create the Comment object
comment = Comment(**comment_data)

# Print the object
print(comment)