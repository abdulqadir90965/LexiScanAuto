import os
import re

INPUT_DIR = "data/annotated_data/raw_text"
OUTPUT_DIR = "data/annotated_data/bio_format"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def tokenize(text):
    # Split words and keep punctuation
    tokens = re.findall(r"\w+|[^\w\s]", text)
    return tokens

for file_name in os.listdir(INPUT_DIR):
    if file_name.endswith(".txt"):
        input_path = os.path.join(INPUT_DIR, file_name)

        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        tokens = tokenize(text)

        output_file = file_name.replace(".txt", ".bio")
        output_path = os.path.join(OUTPUT_DIR, output_file)

        with open(output_path, "w", encoding="utf-8") as f:
            for token in tokens:
                f.write(f"{token} O\n")

        print(f"Created BIO file: {output_file}")

print("Tokenization completed.")
