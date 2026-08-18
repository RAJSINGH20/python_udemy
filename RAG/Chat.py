from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI
import os


# ============================================================
# 1. Load .env file
# ============================================================

load_dotenv()

print("=" * 60)
print("Starting RAG Chat Application")
print("=" * 60)


# ============================================================
# 2. Get OpenRouter API Key
# ============================================================

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY not found in .env file"
    )

print("OpenRouter API key loaded successfully")


# ============================================================
# 3. Create OpenRouter Client
# ============================================================

Client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

print("OpenRouter client initialized")
print("=" * 60)


# ============================================================
# 4. Create Embedding Model
# ============================================================

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

print("Embedding model initialized")


# ============================================================
# 5. Connect to Existing Qdrant Collection
# ============================================================

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)

print("Connected to Qdrant")
print("Collection: learning_rag")
print("=" * 60)


# ============================================================
# 6. Get User Query
# ============================================================

userquery = input("Ask something....... ")

print("\nSearching relevant documents...")


# ============================================================
# 7. Similarity Search
# ============================================================

search_result = vector_db.similarity_search(
    userquery,
    k=4
)

print(f"Found {len(search_result)} relevant chunks")


# ============================================================
# 8. Create Context
# ============================================================

context = "\n\n".join(
    [
        f"""
Page Content:
{result.page_content}

Page Number:
{result.metadata.get("page_label", "Unknown")}

File Location:
{result.metadata.get("source", "Unknown")}
"""
        for result in search_result
    ]
)


# ============================================================
# 9. System Prompt
# ============================================================

system_prompt = """
You are a helpful AI assistant for answering questions from a PDF.

Answer the user's question using the retrieved context.

Format your answer in a clear and easy-to-read way.

Follow this structure:

## Answer
Give a concise and clear explanation.

## Key Points
- Point 1
- Point 2
- Point 3

## Source
Mention the PDF page number where the information was found.

IMPORTANT:
- Do not invent information that is not supported by the context.
- If the context does not contain enough information, clearly say so.
- Keep the answer easy for a beginner to understand.

Retrieved Context:
{context}
"""



# ============================================================
# 10. Send Request to OpenRouter
# ============================================================

print("Generating answer...")

response = Client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": system_prompt.format(
                context=context
            )
        },
        {
            "role": "user",
            "content": userquery
        }
    ]
)


# ============================================================
# 11. Print AI Response
# ============================================================

answer = response.choices[0].message.content

print("\n")
print("=" * 60)
print("AI RESPONSE")
print("=" * 60)

print(answer)

print("=" * 60)


# ============================================================
# 12. Print Retrieved Chunks
# ============================================================

print("\n")
print("=" * 60)
print("RETRIEVED CHUNKS")
print("=" * 60)

for i, result in enumerate(search_result, start=1):

    print(f"\n--- Chunk {i} ---")

    print(
        "Page:",
        result.metadata.get("page_label", "Unknown")
    )

    print(
        "Source:",
        result.metadata.get("source", "Unknown")
    )

    print("Content:")
    print(result.page_content)

    print("-" * 60)