import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel , fields
from typing import Optional


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def getweather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"

    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip()

    return "Weather information could not be retrieved."


system_prompt = """
You are Alexa, a weather assistant.

Your job is to provide current weather information.

When weather information is provided to you, explain it clearly to the user.

Never invent weather information.

If weather information is unavailable, say that the weather service is temporarily unavailable.

Keep your answer concise.
"""




class MyOutput(BaseModel):
    step: str = fields.Field(
        ...,
        description="The ID of the step, example: PLAN or OUTPUT"
    )

    content: Optional[str] = fields.Field(
        None,
        description="The content of the step"
    )

    TOOL: Optional[str] = fields.Field(
        None,
        description="The tool to use"
    )

    INPUT: Optional[str] = fields.Field(
        None,
        description="The input to provide to the tool"
    )
    
while True:
    city = input("Enter city: ")

    weather = getweather(city)

    print("\nWeather API Result:")
    print(weather)

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"Give me the current weather for {city}."
            },
            {
                "role": "system",
                "content": f"Weather API result: {weather}"
            }
        ]
    )

    print("\nAlexa:")
    print(response.choices[0].message.content)