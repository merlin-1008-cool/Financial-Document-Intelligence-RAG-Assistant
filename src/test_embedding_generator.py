from embedding_generator import EmbeddingGenerator

texts = [
    "Applicants must be at least 21 years old.",
    "The minimum annual income requirement is 300000 Indian rupees.",
    "Eligible applicants may apply for personal loans."
]

generator = EmbeddingGenerator()
embeddings = generator.generate_embeddings(texts)

print("Number of texts:", len(texts))
print("Embedding shape:", embeddings.shape)
print("Embedding dimensions:", embeddings.shape[1])
print("First embedding sample:", embeddings[0][:5])
