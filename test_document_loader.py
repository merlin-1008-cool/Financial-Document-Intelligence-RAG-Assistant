from src.document_loader import extract_text_from_pdf

pdf_path = "data/sample_documents/sample_loan_policy.pdf"

pages = extract_text_from_pdf(pdf_path)

print(f"Total pages extracted: {len(pages)}")
print("\nExtracted text:\n")

for page in pages:
    print(f"--- Page {page['page_number']} ---")
    print(page["text"])