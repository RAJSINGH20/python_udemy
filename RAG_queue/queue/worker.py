from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

apikey = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=apikey,
    base_url="https://openrouter.ai/api/v1"
)

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=apikey,
    base_url="https://openrouter.ai/api/v1"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6379",
    collection_name="learning_rag",
    embedding=embedding_model
)


def process_query(query: str):

    print("\nSearching relevant documents...")

    # Search Qdrant
    search_result = vector_db.similarity_search(
        query,
        k=4
    )

    print(f"Found {len(search_result)} relevant chunks")

    # Build context
    context = "\n\n".join(
        [
            f"""
--- Retrieved Chunk {i + 1} ---

Page Content:
{result.page_content}

Page Number:
{result.metadata.get("page_label", result.metadata.get("page", "Unknown"))}

File:
{result.metadata.get("source", "Unknown")}
"""
            for i, result in enumerate(search_result)
        ]
    )

    system_prompt = f"""
You are a helpful AI assistant for answering questions from a PDF.

Answer the user's question using ONLY the retrieved context.

Format your answer exactly like this:

## Answer
Give a clear and beginner-friendly explanation.

## Key Points
- Important point 1
- Important point 2
- Important point 3

## Source
Mention the relevant PDF page number(s).

Rules:
- Do not invent information.
- Do not use knowledge outside the retrieved context.
- If the context does not contain enough information, say:
  "The retrieved PDF content does not contain enough information to answer this question."
- Keep the explanation simple and easy to understand.
- If multiple pages contain relevant information, mention all relevant pages.

Retrieved Context:
{context}
"""

    # Ask LLM
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    # Extract AI answer
    answer = response.choices[0].message.content

    # Display nicely
    print("\n" + "=" * 60)
    print("AI RESPONSE")
    print("=" * 60)

    print(answer)

    print("\n" + "=" * 60)
    print("RETRIEVED CHUNKS")
    print("=" * 60)

    for i, result in enumerate(search_result, 1):
        print(f"\n--- Chunk {i} ---")
        print(f"Page: {result.metadata.get('page_label', 'Unknown')}")
        print(f"Source: {result.metadata.get('source', 'Unknown')}")
        print(f"\n{result.page_content[:500]}...")

    print("=" * 60)
