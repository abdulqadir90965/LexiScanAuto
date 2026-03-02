from spacy.tokens import DocBin
import spacy
from pathlib import Path
import random

nlp = spacy.blank("en")

input_dir = Path("training/corpus")
output_dir = Path("training/corpus")
output_dir.mkdir(parents=True, exist_ok=True)

docs = []

# Load all .spacy files
for spacy_file in input_dir.glob("*.spacy"):
    print(f"Loading: {spacy_file.name}")
    db = DocBin().from_disk(spacy_file)
    docs.extend(list(db.get_docs(nlp.vocab)))

print(f"Total documents loaded: {len(docs)}")

# Shuffle documents
random.shuffle(docs)

# Split 80/20
split = int(len(docs) * 0.8)
train_docs = docs[:split]
dev_docs = docs[split:]

# Save train.spacy
train_db = DocBin(docs=train_docs)
train_db.to_disk(output_dir / "train.spacy")

# Save dev.spacy
dev_db = DocBin(docs=dev_docs)
dev_db.to_disk(output_dir / "dev.spacy")

print("✅ train.spacy and dev.spacy created successfully")
