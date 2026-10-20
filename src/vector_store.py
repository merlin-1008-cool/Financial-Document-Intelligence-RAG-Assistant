import chromadb
from pathlib import Path


class VectorStore:
    """Store and retrieve document chunks using ChromaDB."""

    def __init__(
        self,
        collection_name="financial_documents",
        persist_directory="data/chroma_db"
    ):
        project_dir = Path(__file__).resolve().parent.parent
        storage_path = project_dir / persist_directory

        self.client = chromadb.PersistentClient(
            path=str(storage_path)
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(self, chunks, embeddings):
        """Store text chunks, embeddings, and page metadata."""

        if len(chunks) != len(embeddings):
            raise ValueError(
                "The number of chunks must match the number of embeddings."
            )

        if not chunks:
            return

        ids = [
            f"sample_loan_policy_chunk_{i}"
            for i in range(len(chunks))
        ]

        documents = [chunk["text"] for chunk in chunks]

        metadatas = [
            {"page_number": int(chunk["page_number"])}
            for chunk in chunks
        ]

        self.collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def search(self, query_embedding, n_results=3):
        """Find document chunks most relevant to a query."""

        if self.collection.count() == 0:
            return []

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=min(n_results, self.collection.count())
        )

        matches = []

        for i in range(len(results["ids"][0])):
            matches.append({
                "text": results["documents"][0][i],
                "page_number": results["metadatas"][0][i]["page_number"],
                "distance": results["distances"][0][i]
            })

        return matches
