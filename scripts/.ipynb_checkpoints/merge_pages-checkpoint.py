import os
from collections import defaultdict

INPUT_DIR = "data/ocr_text/cleaned"
OUTPUT_DIR = "data/annotated_data/raw_text"

os.makedirs(OUTPUT_DIR, exist_ok=True)

contracts = defaultdict(list)

# Group pages by contract name
for file_name in os.listdir(INPUT_DIR):
    if file_name.endswith(".txt"):
        contract_name = file_name.split("_page_")[0]
        contracts[contract_name].append(file_name)

# Merge pages
for contract, pages in contracts.items():
    pages.sort()  # ensure correct page order
    merged_text = ""

    for page in pages:
        page_path = os.path.join(INPUT_DIR, page)
        with open(page_path, "r", encoding="utf-8") as f:
            merged_text += f.read() + "\n\n"

    output_path = os.path.join(OUTPUT_DIR, f"{contract}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(merged_text)

    print(f"Merged contract: {contract}")

print("All contracts merged successfully.")
