gt_words = []
ocr_words = []

# read ground truth
with open("ground_truth.txt") as f:
    for line in f:
        parts = line.strip().split(":")
        if len(parts) == 2:
            gt_words.append(parts[1].strip().lower())

# read OCR results
with open("experimental_scripts/ocr_clean.txt") as f:
    for line in f:
        word = line.strip().lower()
        if word != "":
            ocr_words.append(word)

# remove duplicates
ocr_words = list(set(ocr_words))

correct = 0

for word in gt_words:
    if word in ocr_words:
        correct += 1

precision = correct / len(ocr_words)
recall = correct / len(gt_words)
f1 = 2 * precision * recall / (precision + recall)

print("Precision:", round(precision,3))
print("Recall:", round(recall,3))
print("F1 Score:", round(f1,3))