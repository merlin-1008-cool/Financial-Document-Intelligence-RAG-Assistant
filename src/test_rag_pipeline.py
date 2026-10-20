from rag_pipeline import RAGPipeline


# Initialize the RAG pipeline
rag = RAGPipeline()

# Ask a question about the sample loan policy
question = "What is the maximum age limit for a personal loan?"

# Retrieve relevant passages and generate an answer
response = rag.answer_question(question)

print("\nQuestion:")
print(response["question"])

print("\nStatus:")
print(response["message"])

print("\nGenerated Answer:")
print(response["answer"])

print("\nRetrieved Context:")

for i, item in enumerate(response["context"], start=1):
    print(f"\nResult {i}")
    print("Page:", item["page_number"])
    print("Text:", item["text"])
    print("Distance:", round(item["distance"], 4))
