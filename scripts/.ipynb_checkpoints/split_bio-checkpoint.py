import os
import random

INPUT_DIR = "data/annotated_data"
OUTPUT_DIR = "data/split"

random.seed(42)

def read_sentences(path):
    sentences, sentence = [], []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            else:
                sentence.append(line)
        if sentence:
            sentences.append(sentence)
    return sentences

def write_sentences(sentences, path):
    with open(path, "w", encoding="utf-8") as f:
        for s in sentences:
            for l in s:
                f.write(l + "\n")
            f.write("\n")

all_sentences = []

for file in os.listdir(INPUT_DIR):
    if file.endswith(".bio"):
        all_sentences.extend(read_sentences(os.path.join(INPUT_DIR, file)))

random.shuffle(all_sentences)

total = len(all_sentences)
train_end = int(total * 0.8)
val_end = int(total * 0.9)

train = all_sentences[:train_end]
val = all_sentences[train_end:val_end]
test = all_sentences[val_end:]

os.makedirs(OUTPUT_DIR, exist_ok=True)

write_sentences(train, f"{OUTPUT_DIR}/train.bio")
write_sentences(val, f"{OUTPUT_DIR}/valid.bio")
write_sentences(test, f"{OUTPUT_DIR}/test.bio")

print("Split completed")
print("Train:", len(train))
print("Valid:", len(val))
print("Test:", len(test))
