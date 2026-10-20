from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF document.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A list containing the extracted text from each page.
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("The supplied file must be a PDF.")

    reader = PdfReader(str(pdf_path))

    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""

        extracted_pages.append({
            "page_number": page_number,
            "text": page_text.strip()
        })

    return extracted_pages