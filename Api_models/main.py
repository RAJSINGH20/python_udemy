import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()


# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



# Send a chat completion request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ]
)


# Print the AI response
print(response.choices[0].message.content)