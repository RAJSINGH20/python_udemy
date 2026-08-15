from fastapi import FastAPI, Body
from ollama import Client

client = Client(
    host="http://localhost:11434"
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {
        "item_id": item_id,
        "q": q
    }


@app.post("/chat")
def chat(
    message: str = Body(..., description="The message")
):
    response = client.chat(
        model="gemma:2b",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return {
        "response": response.message.content
    }