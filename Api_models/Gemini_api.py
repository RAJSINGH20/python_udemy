import os
from google import genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Explain how the AI API works"
)


# Print response
print(response.text)