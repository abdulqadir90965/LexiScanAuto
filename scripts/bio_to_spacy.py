import spacy
from spacy.tokens import Doc
from pathlib import Path

nlp = spacy.blank("en")

def read_bio_file(file_path):
    sentences = []
    words = []
    labels = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                if words:
                    sentences.append((words, labels))
                    words = []
                    labels = []
            else:
                token, tag = line.split()
                words.append(token)
                labels.append(tag)

    if words:
        sentences.append((words, labels))

    return sentences


def convert_bio_to_spacy(input_path, output_path):
    docs = []

    sentences = read_bio_file(input_path)

    for words, labels in sentences:
        doc = Doc(nlp.vocab, words=words)
        ents = []

        start = 0
        for i, label in enumerate(labels):
            if label.startswith("B-"):
                ent_label = label[2:]
                ent_start = doc[i].idx
                ent_end = ent_start + len(doc[i].text)

                j = i + 1
                while j < len(labels) and labels[j].startswith("I-"):
                    ent_end = doc[j].idx + len(doc[j].text)
                    j += 1

                ents.append((ent_start, ent_end, ent_label))

        doc.ents = [doc.char_span(s, e, label=l) for s, e, l in ents if doc.char_span(s, e, label=l)]
        docs.append(doc)

    doc_bin = spacy.tokens.DocBin(docs=docs)
    doc_bin.to_disk(output_path)


input_dir = Path("data/raw_bio")
output_dir = Path("data/spacy_format")
output_dir.mkdir(exist_ok=True)

for bio_file in input_dir.glob("*.bio"):
    output_file = output_dir / f"{bio_file.stem}.spacy"
    convert_bio_to_spacy(bio_file, output_file)
    print(f"Converted {bio_file.name} → {output_file.name}")
