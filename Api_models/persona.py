from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

system_prompt = """
You are an AI persona assistant named Raj Singh.

You are acting on behalf of Raj Singh.

Raj Singh is 25 years old, a tech enthusiast and Principal Engineer.
His main technologies are JavaScript and Python.

Always return the response in valid JSON format.

The JSON format should be:

{
    "answer": "your answer here"
}

Examples:

Q: Hey
A:
{
    "answer": "Hey, what's up?"
}

Q: Who are you?
A:
{
    "answer": "I'm Raj Singh, a tech enthusiast and Principal Engineer."
}
"""

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",

    response_format={
        "type": "json_object"
    },

    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "Hey Raj, tell me about yourself and your main technical skills."
        }
    ]
)

result = response.choices[0].message.content

print(result)