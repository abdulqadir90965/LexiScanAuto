from pdf2image import convert_from_path
import os

# Input and output folders
PDF_DIR = "data/raw_pdfs"
IMAGE_DIR = "data/images"

# Create output folder if it doesn't exist
os.makedirs(IMAGE_DIR, exist_ok=True)

# Loop through all PDFs
for pdf_file in os.listdir(PDF_DIR):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(PDF_DIR, pdf_file)

        print(f"Processing: {pdf_file}")

        # Convert PDF to images
        pages = convert_from_path(pdf_path, dpi=300)

        # Save each page as image
        for i, page in enumerate(pages):
            image_name = f"{pdf_file.replace('.pdf','')}_page_{i+1}.png"
            image_path = os.path.join(IMAGE_DIR, image_name)
            page.save(image_path, "PNG")

        print(f"Saved {len(pages)} pages for {pdf_file}")
