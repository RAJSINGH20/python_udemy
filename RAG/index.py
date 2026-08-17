from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

# ============================================================
# 1. Load environment variables from .env file
# ============================================================

load_dotenv()

print("Starting RAG document indexing...")
print("=" * 60)


# ============================================================
# 2. Locate the PDF file
# ============================================================

# Get the directory where this Python file is located
pdf_path = Path(__file__).parent / "node-js.pdf"

print(f"PDF Path: {pdf_path}")

# Check whether the PDF exists
if not pdf_path.exists():
    raise FileNotFoundError(f"PDF file not found: {pdf_path}")

print("PDF file found successfully!")
print("=" * 60)


# ============================================================
# 3. Load the PDF
# ============================================================

print("Loading PDF...")

loader = PyPDFLoader(file_path=str(pdf_path))

# Load every page of the PDF as a Document object
docs = loader.load()

print("PDF loaded successfully!")
print(f"Total pages loaded: {len(docs)}")
print("=" * 60)


# ============================================================
# 4. Display an example document
# ============================================================

print("Displaying document from page/index 12:")
print("-" * 60)

print(docs[12])

print("-" * 60)
print("=" * 60)


# ============================================================
# 5. Split documents into smaller chunks
# ============================================================

print("Splitting documents into smaller chunks...")

# RecursiveCharacterTextSplitter divides large documents
# into smaller pieces that are easier for the embedding model
# and LLM to process.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

print("Document splitting completed!")
print(f"Original documents/pages : {len(docs)}")
print(f"Total chunks created     : {len(chunks)}")
print("=" * 60)


# ============================================================
# 6. Display the first chunk
# ============================================================

print("Displaying the first chunk:")
print("-" * 60)

print(chunks[0])

print("-" * 60)
print("=" * 60)


# ============================================================
# 7. Create the embedding model
# ============================================================

print("Initializing OpenAI embedding model...")

# OpenRouter is used as the API provider.
# The API key is loaded from the .env file.
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

print("Embedding model initialized successfully!")
print("Model: text-embedding-3-large")
print("=" * 60)


# ============================================================
# 8. Store embeddings in Qdrant
# ============================================================

print("Connecting to Qdrant...")
print("Creating embeddings and storing them in Qdrant...")

# Convert every document chunk into an embedding
# and store the vectors inside the Qdrant collection.
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("Embeddings successfully stored in Qdrant!")
print("=" * 60)


# ============================================================
# 9. Indexing completed
# ============================================================

print("INDEXING COMPLETED SUCCESSFULLY!")
print(f"Pages processed : {len(docs)}")
print(f"Chunks indexed  : {len(chunks)}")
print("Qdrant collection: learning_rag")
print("Qdrant URL        : http://localhost:6333")
print("=" * 60)