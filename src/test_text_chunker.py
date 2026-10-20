from text_chunker import chunk_text

sample_text = "Sample Bank - Personal Loan Policy. " * 20

pages = [{"page_number": 1, "text": sample_text}]
chunks = chunk_text(pages)

print("Total chunks created:", len(chunks))
for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)
