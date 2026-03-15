import cv2
import easyocr
import os
import re

reader = easyocr.Reader(['en'], gpu=False)

image_folder = "images/test"

# =========================
# LOAD GROUND TRUTH
# =========================

ground_truth = {}

with open("ground_truth.txt") as f:
    for line in f:
        parts = line.strip().split(":")
        if len(parts) != 2:
            continue

        name = parts[0].strip()
        label = parts[1].strip().lower()

        label = re.sub(r'[^a-z0-9]', '', label)

        prefix = name.split("_")[0]

        ground_truth[prefix] = label

TP = 0
FP = 0
FN = 0

# =========================
# PROCESS IMAGES
# =========================

for img_name in list(os.listdir(image_folder))[:100]:

    prefix = img_name.split("_")[0]

    if prefix not in ground_truth:
        continue

    true_word = ground_truth[prefix]

    img_path = os.path.join(image_folder, img_name)
    image = cv2.imread(img_path)

    results = reader.readtext(image)

    predicted_words = []

    for (_, text, conf) in results:
        clean = re.sub(r'[^a-z0-9]', '', text.lower())
        predicted_words.append(clean)

    if any(true_word in p or p in true_word for p in predicted_words):
        TP += 1
    elif len(predicted_words) > 0:
        FP += 1
    else:
        FN += 1

# =========================
# CALCULATE METRICS
# =========================

precision = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0

print("\n===== OCR Evaluation Metrics =====")
print("True Positives:", TP)
print("False Positives:", FP)
print("False Negatives:", FN)

print(f"\nPrecision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")