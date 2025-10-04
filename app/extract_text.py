import os
import fitz  # PyMuPDF

DATA_DIR = "data"
OUTPUT_DIR = "docs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text

def process_all_pdfs():
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(DATA_DIR, filename)
            print(f"Processing {filename}...")

            text = extract_text_from_pdf(pdf_path)

            # Save as .txt
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".txt"))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Saved text to {output_path}")

if __name__ == "__main__":
    process_all_pdfs()