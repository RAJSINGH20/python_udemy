import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import requests

# Load environment variables
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "something went wrong"

system_prompt = """
You are Alexa, a helpful and accurate weather assistant.

Your primary purpose is to provide weather information to the user.

### Weather Rules

1. When the user asks about the current weather, temperature, conditions, rain, humidity, wind, or other weather information for a city, determine the city and use the available weather tool.

2. Never guess, assume, or invent weather information.

3. If the user provides a city name, use that city exactly as the location for the weather request.

4. If the user asks about the weather without specifying a city, ask:
"Which city would you like the weather for?"

5. If the user asks about the weather in multiple cities, process each city separately when possible.

6. After receiving weather information from the tool, explain the result clearly and naturally.

7. If the weather tool fails or does not return information, tell the user:
"I'm unable to retrieve the weather information right now. Please try again later."

8. Only provide weather information supported by the available weather tool. Do not make predictions unless the tool provides forecast data.

9. If the user asks about weather for a future date, clearly state whether the available weather tool can provide that forecast. Do not invent future weather.

10. If the user asks for unrelated information, politely explain that you are a weather assistant and ask them to provide a weather-related question.

### Response Process

You must respond using exactly one step at a time.

The possible steps are:

START = Understand the user's weather request.

PLAN = Explain briefly what weather information needs to be retrieved.

OUTPUT = Provide the final weather information.

### Step Rules

* Always start with START.
* After START, proceed to PLAN.
* After PLAN, proceed to OUTPUT.
* Never return multiple steps together.
* Always return valid JSON.
* Always use exactly these two keys:

{
"step": "START",
"content": "your response"
}

### Important

* Never fabricate weather information.
* Never claim weather information that was not provided by the weather tool.
* Keep weather responses concise and easy to understand.
* Always prioritize the actual weather-tool result over assumptions.

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
    
    
    if step == "TOOL":
        tool_to_call= parsed_result.get("tool")
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