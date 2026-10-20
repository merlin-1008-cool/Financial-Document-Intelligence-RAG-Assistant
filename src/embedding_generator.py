from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """Generate numerical embeddings for financial document text."""

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, texts):
        """Convert text strings into numerical embeddings."""

        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=False
        )

        return embeddings
