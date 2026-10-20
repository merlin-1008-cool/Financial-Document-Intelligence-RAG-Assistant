from pathlib import Path

from document_loader import extract_text_from_pdf
from text_chunker import chunk_text
from embedding_generator import EmbeddingGenerator
from vector_store import VectorStore


# Locate the sample financial PDF
project_dir = Path(__file__).resolve().parent.parent

pdf_path = (
    project_dir
    / "data"
    / "sample_documents"
    / "sample_loan_policy.pdf"
)

# Step 1: Extract text from the PDF
pages = extract_text_from_pdf(str(pdf_path))
chunks = chunk_text(pages)

print("PDF pages extracted:", len(pages))
print("Text chunks created:", len(chunks))

if not chunks:
    raise ValueError("No text chunks were created from the PDF.")

# Step 2: Generate embeddings
generator = EmbeddingGenerator()

texts = [chunk["text"] for chunk in chunks]
embeddings = generator.generate_embeddings(texts)

print("Embeddings generated:", embeddings.shape)

# Step 3: Reset the test collection
# WARNING: This deletes the existing financial_documents collection.
vector_store = VectorStore()

vector_store.client.delete_collection(
    name="financial_documents"
)

vector_store = VectorStore()
vector_store.add_documents(chunks, embeddings)

print(
    "Documents stored in ChromaDB:",
    vector_store.collection.count()
)

# Step 4: Search for relevant information
query = "What is the minimum annual income required for a personal loan?"

query_embedding = generator.generate_embeddings([query])[0]

results = vector_store.search(
    query_embedding,
    n_results=2
)

print("\nSearch results:")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Page:", result["page_number"])
    print("Text:", result["text"])
    print("Distance:", round(result["distance"], 4))
