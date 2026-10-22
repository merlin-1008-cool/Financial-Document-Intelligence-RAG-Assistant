from pathlib import Path
import sys
import requests

# Allow imports from the src directory
SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from embedding_generator import EmbeddingGenerator
from vector_store import VectorStore
from document_loader import extract_text_from_pdf
from text_chunker import chunk_text


class RAGPipeline:
    """Retrieve financial document passages and generate answers using Gemma."""

    def __init__(self):
        self.embedding_generator = EmbeddingGenerator()

        self.vector_store = VectorStore()

        project_dir = Path(__file__).resolve().parent.parent

        
        pdf_path = project_dir / "data" / "sample_documents" / "sample_loan_policy.pdf"

        # Populate ChromaDB if the collection is empty

        if self.vector_store.collection.count() == 0:

            pages = extract_text_from_pdf(pdf_path)

            chunks = chunk_text(pages)

            if chunks:

                texts = [chunk["text"] for chunk in chunks]

                embeddings = self.embedding_generator.generate_embeddings(texts)

                self.vector_store.add_documents(chunks, embeddings)

        self.ollama_url = "http://localhost:11434/api/generate"

        self.model = "gemma4:e2b"
        

    def answer_question(self, question, top_k=3):
        """Retrieve relevant passages and generate an answer using Ollama."""

        if not question or not question.strip():
            return {
                "question": question,
                "context": [],
                "answer": "",
                "message": "Please enter a question."
            }

        # Generate an embedding for the question
        query_embedding = (
            self.embedding_generator.generate_embeddings(
                [question]
            )[0]
        )

        # Retrieve relevant passages from ChromaDB
        results = self.vector_store.search(
            query_embedding=query_embedding,
            n_results=top_k
        )

        # Prepare the retrieved passages
        context = []

        for result in results:
            context.append({
                "text": result["text"],
                "page_number": result["page_number"],
                "source": result.get("source"),
                "distance": result["distance"]
            })

        if not context:
            return {
                "question": question,
                "context": [],
                "answer": "",
                "message": "No relevant passages were found."
            }

        # Combine retrieved passages into context
        context_text = "\n\n".join(
            f"Source: {item['source']}\n"
            f"Page: {item['page_number']}\n"
            f"Text: {item['text']}"
            for item in context
        )

        # Build a prompt grounded in the retrieved documents
        prompt = f"""
You are a financial document assistant.
Answer the question using only the context provided below.
If the context does not contain the answer, say that the
provided documents do not contain enough information.
Do not invent financial policies or requirements.

Context:
{context_text}

Question:
{question}

Answer:
"""

        try:
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )
            response.raise_for_status()
            answer = response.json()["response"].strip()

            message = "Relevant passages retrieved and answer generated successfully."

        except requests.RequestException as error:
            answer = ""
            message = f"Passages retrieved, but answer generation failed: {error}"

        return {
            "question": question,
            "context": context,
            "answer": answer,
            "message": message
        }
