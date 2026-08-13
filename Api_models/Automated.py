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

You must ALWAYS return valid JSON.

Return ONLY one step at a time.

The JSON format MUST be:

{
    "step": "START",
    "content": "your response"
}

The possible steps are:

START = Understand the user's question.

PLAN = Explain the approach or plan for answering.

OUTPUT = Give the final answer.

Rules for steps:

- First return START.
- Then return PLAN.
- Finally return OUTPUT.
- Never return START, PLAN, and OUTPUT together.
- Always use exactly these keys:
"step"
"content"
"""

# Message history
message_history = [
    {
        "role": "system",
        "content": system_prompt
    }
]

# Get user input
user_query = input("Input the text: ")

message_history.append({
    "role": "user",
    "content": user_query
})

# Automated process
while True:

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=message_history
    )

    # Get model response
    raw_result = response.choices[0].message.content

    print("\nRaw response:")
    print(raw_result)

    # Add assistant response to history
    message_history.append({
        "role": "assistant",
        "content": raw_result
    }) 

    # Convert JSON string into Python dictionary
    try:
        parsed_result = json.loads(raw_result)
    except json.JSONDecodeError:
        print("Invalid JSON received from model.")
        break

    # Get step
    step = parsed_result.get("step")
    content = parsed_result.get("content")

    # START
    if step == "START":

        print("\nSTART:")
        print(content)

        message_history.append({
            "role": "user",
            "content": "Now proceed to the PLAN step."
        })

        continue

    # PLAN
    if step == "PLAN":

        print("\nPLAN:")
        print(content)

        message_history.append({
            "role": "user",
            "content": "Now proceed to the OUTPUT step and give the final answer."
        })

        continue

    # OUTPUT
    if step == "OUTPUT":

        print("\nOUTPUT:")
        print(content)

        break

    # Unknown step
    print("Unknown step received:", step)
    break