from pathlib import Path
import os
import sys

import streamlit as st
from groq import Groq

# Allow imports from the src directory
SRC_DIR = Path(__file__).resolve().parent

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from embedding_generator import EmbeddingGenerator
from vector_store import VectorStore
from document_loader import extract_text_from_pdf
from text_chunker import chunk_text


class RAGPipeline:
    """Retrieve financial document passages and generate answers using Groq."""

    def __init__(self):
        # Initialize embeddings and vector storage
        self.embedding_generator = EmbeddingGenerator()
        self.vector_store = VectorStore()

        # Read the Groq API key from Streamlit Secrets or environment
        try:
            self.api_key = (
                st.secrets.get("GROQ_API_KEY")
                or os.environ.get("GROQ_API_KEY")
            )
        except Exception:
            self.api_key = os.environ.get("GROQ_API_KEY")

        # Initialize Groq only when an API key is available
        self.client = Groq(api_key=self.api_key) if self.api_key else None

        # Groq model
        self.model = "openai/gpt-oss-120b"

        # Locate the sample PDF
        project_dir = Path(__file__).resolve().parent.parent

        pdf_path = (
            project_dir
            / "data"
            / "sample_documents"
            / "sample_loan_policy.pdf"
        )

        # Populate ChromaDB if the collection is empty
        if self.vector_store.collection.count() == 0:
            if not pdf_path.exists():
                raise FileNotFoundError(
                    f"PDF file not found: {pdf_path}"
                )

            pages = extract_text_from_pdf(pdf_path)
            chunks = chunk_text(pages)

            if chunks:
                texts = [chunk["text"] for chunk in chunks]

                embeddings = (
                    self.embedding_generator.generate_embeddings(texts)
                )

                self.vector_store.add_documents(chunks, embeddings)

    def answer_question(self, question, top_k=3):
        """Retrieve relevant passages and generate an answer using Groq."""

        if not question or not question.strip():
            return {
                "question": question,
                "context": [],
                "answer": "",
                "message": "Please enter a question.",
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
            n_results=top_k,
        )

        # Prepare retrieved passages
        context = []

        for result in results:
            context.append(
                {
                    "text": result["text"],
                    "page_number": result["page_number"],
                    "source": result.get("source"),
                    "distance": result["distance"],
                }
            )

        if not context:
            return {
                "question": question,
                "context": [],
                "answer": "",
                "message": "No relevant passages were found.",
            }

        # Combine retrieved passages into context
        context_text = "\n\n".join(
            f"Source: {item['source']}\n"
            f"Page: {item['page_number']}\n"
            f"Text: {item['text']}"
            for item in context
        )

        # Check whether the Groq API key is configured
        if self.client is None:
            return {
                "question": question,
                "context": context,
                "answer": "",
                "message": (
                    "Passages retrieved, but answer generation failed: "
                    "GROQ_API_KEY is not configured. "
                    "Check Streamlit Cloud Secrets."
                ),
            }

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a financial document assistant. "
                            "Answer using only the supplied document context. "
                            "If the answer is not in the context, state that "
                            "the provided documents do not contain enough "
                            "information. Do not invent financial policies."
                        ),
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Context:\n{context_text}\n\n"
                            f"Question:\n{question}"
                        ),
                    },
                ],
                temperature=0,
            )

            answer = (
                response.choices[0].message.content or ""
            ).strip()

            message = (
                "Relevant passages retrieved and answer generated successfully."
            )

        except Exception as error:
            answer = ""
            message = (
                "Passages retrieved, but answer generation failed: "
                f"{error}"
            )

        return {
            "question": question,
            "context": context,
            "answer": answer,
            "message": message,
        }
