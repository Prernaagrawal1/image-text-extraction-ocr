import re

cleaned_lines = []

with open("ocr_results.txt", "r", encoding="utf-8") as f:
    for line in f:
        text = re.sub(r'\(.*?\)', '', line)  # remove confidence scores
        text = text.strip()

        if text != "":
            cleaned_lines.append(text)

with open("ocr_clean.txt", "w", encoding="utf-8") as f:
    for line in cleaned_lines:
        f.write(line + "\n")

print("Cleaned OCR results saved to ocr_clean.txt")