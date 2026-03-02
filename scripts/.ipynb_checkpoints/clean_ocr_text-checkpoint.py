import os
import re

INPUT_DIR = "data/ocr_text"
CLEAN_DIR = "data/ocr_text/cleaned"

os.makedirs(CLEAN_DIR, exist_ok=True)

def clean_text(text):
    # Remove non-printable characters
    text = re.sub(r"[^\x20-\x7E]", " ", text)

    # Replace multiple spaces with single space
    text = re.sub(r"\s+", " ", text)

    # Fix broken lines
    text = text.replace(" .", ".")
    text = text.replace(" ,", ",")

    return text.strip()

for file_name in os.listdir(INPUT_DIR):
    if file_name.endswith(".txt"):
        input_path = os.path.join(INPUT_DIR, file_name)

        with open(input_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned_text = clean_text(raw_text)

        output_path = os.path.join(CLEAN_DIR, file_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        print(f"Cleaned: {file_name}")

print("All OCR text cleaned successfully.")
