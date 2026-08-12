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

# System prompt
system_prompt = """
You are Alexa.
Give only study-related answers.
If the user asks something that is not related to studies,
just say: "Sorry, I can only answer study-related questions."
"""

# Send request
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "pizza"
        }
    ]
)

# Print response
print(response.choices[0].message.content)

# Zero-shot prompting means directly giving an instruction
# to the model without providing any examples.