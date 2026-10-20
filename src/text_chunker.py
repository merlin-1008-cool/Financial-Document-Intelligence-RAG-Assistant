def chunk_text(pages, chunk_size=500, overlap=100):
    """
    Split extracted PDF pages into smaller text chunks.

    Args:
        pages: List of dictionaries containing page_number and text.
        chunk_size: Maximum number of characters per chunk.
        overlap: Number of overlapping characters between chunks.

    Returns:
        A list of text chunks with their source page numbers.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size.")

    chunks = []

    for page in pages:
        text = page["text"]
        page_number = page["page_number"]

        start = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk = text[start:end].strip()

            if chunk:
                chunks.append({
                    "page_number": page_number,
                    "text": chunk
                })

            if end == len(text):
                break

            start = end - overlap

    return chunks