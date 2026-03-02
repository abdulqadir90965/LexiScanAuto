import pytesseract
from PIL import Image
import os

# If Tesseract is not in PATH, uncomment and set path manually
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

IMAGE_DIR = "data/images"
TEXT_DIR = "data/ocr_text"

os.makedirs(TEXT_DIR, exist_ok=True)

for image_file in os.listdir(IMAGE_DIR):
    if image_file.endswith(".png"):
        image_path = os.path.join(IMAGE_DIR, image_file)

        print(f"OCR Processing: {image_file}")

        # Open image
        img = Image.open(image_path)

        # Extract text
        extracted_text = pytesseract.image_to_string(img)

        # Save text
        text_file_name = image_file.replace(".png", ".txt")
        text_path = os.path.join(TEXT_DIR, text_file_name)

        with open(text_path, "w", encoding="utf-8") as f:
            f.write(extracted_text)

print("OCR completed for all images.")
