import os
from pdfminer.high_level import extract_text

def convert_pdf(pdf_path):
    txt_path = pdf_path.replace(".pdf", ".txt")
    filename = os.path.basename(pdf_path)
    try:
        text = extract_text(pdf_path)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Converted {filename}")
    except Exception as e:
        print(f"Failed: {filename} ({e})")


def convert_all_pdfs_in_current_dir():
    current_dir = os.getcwd()

    for filename in os.listdir(current_dir):
        if filename.endswith(".pdf"):
            full_path = os.path.join(current_dir, filename)
            convert_pdf(full_path)

if __name__ == "__main__":
    convert_all_pdfs_in_current_dir()
