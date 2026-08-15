from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(
    r"C:\Users\rajsi\Desktop\python_udemy\Weather_AGENT\.env",
    override=True
)

api_key = os.getenv("OPENAI_API_KEY")

print("API key loaded:", bool(api_key))
print("Key prefix:", api_key[:7] if api_key else "NONE")

client = OpenAI(api_key=api_key)


def main():
    user_query = input("> ")

    response = client.responses.create(
        model="gpt-5",
        input=user_query
    )

    print(response.output_text)


if __name__ == "__main__":
    main()