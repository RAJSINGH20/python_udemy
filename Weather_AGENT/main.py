from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
# https://wttr.in/{city}?format=%C+%t

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GPT"),
    # base_url="https://openrouter.ai/api/v1"
)

# def getwheather(city:str):
#     url = "https://wttr.in/{city}?format=%C+%t"
#     response = requests.get(url)

#     if response.status_code == 200:
#         return response.text
#     else:
#         return "somthing went wrong"
# print(getwheather("london"))

def main():
    user_query = input("> ")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()