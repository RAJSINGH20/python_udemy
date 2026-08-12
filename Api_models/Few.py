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

# System prompt with few-shot examples
system_prompt = """
You are Alexa, a helpful study assistant.

Rules:
1. Answer the user's questions clearly and accurately.
2. Give simple explanations.
3. For programming questions, provide code examples when useful.
4. For study-related questions, explain the topic step by step.
5. Do not refuse questions just because they are not study-related.
6. If the user asks your name, answer: "My name is Alexa.".
"""

message_history = {
    { "role":"system","content":system_prompt}
}

user_query=  input("input the text :")
message_history.append({"role":"user","content":user_query})


# Send request
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        

        # User example
        {
            "role": "user",
            "content": "give a short note on Python?"
        },

        # Assistant example
        {
            "role": "assistant",
            "content": json.dumps({
                "step": "START",
                "content": "Python is a high-level programming language used for web development, AI, data science, and automation."
            })
        },
        {
            "role": "user",
            "content": "write a code with n number of element in javascript"
        }

        # Actual user question
        
    ]
)

# Print response
print(response.choices[0].message.content)

# Few-shot prompting means providing examples to the model
# before giving the actual task.