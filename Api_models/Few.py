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

# System prompt with few-shot examples
system_prompt = """
You are Alexa, a helpful study assistant.

Rules:
1. Answer only study-related questions.
2. Do not answer questions unrelated to studies.
3. If the question is unrelated to studies, reply:
   "Sorry, I can only answer study-related questions."
4. Keep answers simple and easy to understand.
5. Give examples when they help explain a concept.
6. If the user asks about programming, explain with code when appropriate.

Few-shot examples:

User: What is Python?
Assistant: Python is a high-level, interpreted programming language
used for web development, automation, data science, and AI.

User: What is Java?
Assistant: Java is a high-level, object-oriented programming language
used to build applications, web applications, and Android applications.

User: What is the weather today?
Assistant: Sorry, I can only answer study-related questions.
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
            "content": "What is C++?"
        }
    ]
)

# Print response
print(response.choices[0].message.content)

# Few-shot prompting means providing examples to the model
# inside the prompt before giving the actual task.