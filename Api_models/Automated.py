import os
import json
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
You are Alexa, a helpful study assistant.

Rules:
1. Answer the user's questions clearly and accurately.
2. Give simple explanations.
3. For programming questions, provide code examples when useful.
4. For study-related questions, explain the topic step by step.
5. Do not refuse questions just because they are not study-related.
6. If the user asks your name, answer: "My name is Alexa."

Always return valid JSON.

Use:
START = understand the question
PLAN = explain the approach
OUTPUT = give the final answer

After START or PLAN, you must eventually return OUTPUT.
"""

message_history = [
    {
        "role": "system",
        "content": system_prompt
    }
]

user_query = input("input the text: ")

message_history.append({
    "role": "user",
    "content": user_query
})

while True:
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=message_history
    )

    raw_result = response.choices[0].message.content

    message_history.append({
        "role": "assistant",
        "content": raw_result
    })

    Parsed_result = json.loads(raw_result)

    if Parsed_result.get("step") == "START":
        print(Parsed_result.get("content"))

        message_history.append({
            "role": "user",
            "content": "Now proceed to the next step."
        })
        continue

    if Parsed_result.get("step") == "PLAN":
        print(Parsed_result.get("content"))

        message_history.append({
            "role": "user",
            "content": "Now provide the final answer."
        })
        continue

    if Parsed_result.get("step") == "OUTPUT":
        print(Parsed_result.get("content"))
        break