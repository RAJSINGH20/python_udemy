from openai import OpenAI
import dotenv
dotenv.load_dotenv()

APIKEY = dotenv.get_key(dotenv.find_dotenv(), "apikey")

client = OpenAI(
    api_key=APIKEY,
    base_url="https://openrouter.ai/api/v1"
)

res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIskXiis51E9dy9AuCWVRoGU_4sUYlwfjJUbFWRyESxA&s"
                    }
                }
            ]
        }
    ]
)

print(res.choices[0].message.content)