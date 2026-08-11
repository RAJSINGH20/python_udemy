import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()


# Create OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

while True:
    user = input("enter the string : \n")

    # Send a request

    if user == "STOP":
        break
    else:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": user
                }
            ]
        )


# Print response
print(response.choices[0].message.content)
