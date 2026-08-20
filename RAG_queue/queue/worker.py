from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI
import os


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

print("API key loaded successfully")


# ============================================================
# OPENROUTER
# ============================================================

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

print("OpenRouter client initialized")


# ============================================================
# EMBEDDINGS
# ============================================================

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

print("Embedding model initialized")


# ============================================================
# QDRANT
# ============================================================

print("Connecting to Qdrant...")

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)

print("Connected to Qdrant successfully")


# ============================================================
# STEP 1
# QUERY UNDERSTANDING
# ============================================================

def understand_query(user_query: str):

    prompt = f"""
You are a query understanding system for a PDF-based RAG system.

The PDF is about Node.js.

The user entered:

"{user_query}"

Convert the user's input into a clear and specific search query.

Rules:

1. Preserve the user's original intent.
2. If the query is very short, expand it.
3. If the user says "node", understand it as "Node.js".
4. If the user asks about a concept, make the query specific.
5. Do not answer the question.
6. Return ONLY the improved search query.

Examples:

User: node
Output: What is Node.js?

User: async
Output: What is asynchronous programming in Node.js?

User: event loop
Output: What is the event loop in Node.js?

User: why node
Output: Why should Node.js be used?

User: modules
Output: What are Node.js modules and how do they work?

User: {user_query}
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ],
        temperature=0
    )

    improved_query = response.choices[0].message.content.strip()

    return improved_query


# ============================================================
# STEP 2
# QDRANT RETRIEVAL
# ============================================================

def retrieve_documents(search_query: str):

    print("\nSearching Qdrant...")

    results = vector_db.similarity_search_with_score(
        search_query,
        k=8
    )

    print(f"Retrieved {len(results)} chunks")

    return results


# ============================================================
# STEP 3
# FILTER / RERANK
# ============================================================

def rerank_documents(results):

    print("\nRe-ranking retrieved chunks...")

    # similarity_search_with_score returns:
    #
    # (Document, score)
    #
    # For Qdrant cosine similarity, higher score
    # generally means more similar.

    sorted_results = sorted(
        results,
        key=lambda x: x[1],
        reverse=True
    )

    # Keep the best 5 chunks
    filtered_results = sorted_results[:5]

    print(f"Selected {len(filtered_results)} best chunks")

    return filtered_results


# ============================================================
# STEP 4
# BUILD CONTEXT
# ============================================================

def build_context(results):

    context_parts = []

    for i, (document, score) in enumerate(results, 1):

        page = document.metadata.get(
            "page_label",
            document.metadata.get(
                "page",
                "Unknown"
            )
        )

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        content = document.page_content

        context_parts.append(
            f"""
============================================================
SOURCE {i}
============================================================

Page: {page}

File: {source}

Relevance Score: {score}

Content:
{content}
"""
        )

    return "\n".join(context_parts)


# ============================================================
# STEP 5
# GROUNDED LLM ANSWER
# ============================================================

def generate_answer(
    original_query,
    improved_query,
    context
):

    system_prompt = f"""
You are a highly accurate PDF RAG assistant.

You MUST answer the user's question using ONLY the
retrieved PDF context provided below.

IMPORTANT RULES:

1. Do NOT use your outside knowledge.
2. Do NOT hallucinate.
3. Every factual statement must be supported by the retrieved context.
4. If the retrieved context does not contain enough information,
   clearly say that the PDF does not provide enough information.
5. Prefer information that directly answers the question.
6. Do not confuse table-of-contents pages with actual explanatory content.
7. If multiple pages support the answer, mention all relevant pages.
8. Keep the explanation beginner-friendly.
9. Do not mention the retrieval process unless necessary.

USER QUERY:

{original_query}

IMPROVED SEARCH QUERY:

{improved_query}

RETRIEVED PDF CONTEXT:

{context}

Return the answer using EXACTLY this structure:

## Answer

[Clear answer based only on the PDF]

## Key Points

- [Important point]
- [Important point]
- [Important point]

## Source

[Relevant PDF page numbers]
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


# ============================================================
# COMPLETE RAG PIPELINE
# ============================================================

def process_query(user_query: str):

    print("\n")
    print("=" * 60)
    print("USER QUERY")
    print("=" * 60)
    print(user_query)


    # --------------------------------------------------------
    # QUERY UNDERSTANDING
    # --------------------------------------------------------

    print("\nUnderstanding query...")

    improved_query = understand_query(user_query)

    print("\nImproved Search Query:")
    print(improved_query)


    # --------------------------------------------------------
    # RETRIEVAL
    # --------------------------------------------------------

    results = retrieve_documents(improved_query)


    # --------------------------------------------------------
    # RERANKING
    # --------------------------------------------------------

    results = rerank_documents(results)


    # --------------------------------------------------------
    # BUILD CONTEXT
    # --------------------------------------------------------

    context = build_context(results)


    # --------------------------------------------------------
    # GENERATE ANSWER
    # --------------------------------------------------------

    print("\nGenerating AI response...")

    answer = generate_answer(
        user_query,
        improved_query,
        context
    )


    # --------------------------------------------------------
    # DISPLAY ANSWER
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("AI RESPONSE")
    print("=" * 60)

    print(answer)


    # --------------------------------------------------------
    # DISPLAY RETRIEVED DOCUMENTS
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("RETRIEVED / RERANKED CHUNKS")
    print("=" * 60)

    for i, (document, score) in enumerate(results, 1):

        page = document.metadata.get(
            "page_label",
            document.metadata.get(
                "page",
                "Unknown"
            )
        )

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        print(f"\n--- Chunk {i} ---")
        print(f"Page: {page}")
        print(f"Score: {score}")
        print(f"Source: {source}")

        print("\nContent:")
        print(document.page_content[:700])

        print("-" * 60)


# ============================================================
# INTERACTIVE TERMINAL
# ============================================================

if __name__ == "__main__":

    while True:

        query = input(
            "\nAsk your question (type 'exit' to quit): "
        ).strip()

        if not query:
            continue

        if query.lower() == "exit":
            print("\nGoodbye!")
            break

        process_query(query)