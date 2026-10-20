from pathlib import Path
from document_loader import extract_text_from_pdf
from text_chunker import chunk_text

project_dir = Path(__file__).resolve().parent.parent
pdf_path = project_dir / "data" / "sample_documents" / "sample_loan_policy.pdf"

if not pdf_path.exists():
    raise FileNotFoundError("PDF not found: " + str(pdf_path))

pages = extract_text_from_pdf(str(pdf_path))

print("PDF loaded successfully.")
print("Total pages extracted:", len(pages))

chunks = chunk_text(pages)

print("Total chunks created:", len(chunks))

if chunks:
    print("\nFirst chunk:")
    print(chunks[0])
else:
    print("No chunks were created.")
