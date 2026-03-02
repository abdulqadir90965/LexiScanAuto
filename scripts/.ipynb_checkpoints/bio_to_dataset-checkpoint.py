import pickle

def load_bio(path):
    data, tokens, labels = [], [], []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                if tokens:
                    data.append((tokens, labels))
                    tokens, labels = [], []
            else:
                token, label = line.split()
                tokens.append(token)
                labels.append(label)
        if tokens:
            data.append((tokens, labels))
    return data

for split in ["train", "valid", "test"]:
    data = load_bio(f"data/split/{split}.bio")
    with open(f"data/processed/{split}.pkl", "wb") as f:
        pickle.dump(data, f)

print("BIO → model-ready conversion done")
