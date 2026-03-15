import cv2
import easyocr
import os
import time

reader = easyocr.Reader(['en'], gpu=False)

image_folder = "images/test"

total_time = 0
image_count = 0
detections = 0

# process only first 100 images
for img_name in list(os.listdir(image_folder))[:100]:

    img_path = os.path.join(image_folder, img_name)

    # skip non-image files
    if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    image = cv2.imread(img_path)

    if image is None:
        continue

    start = time.time()
    results = reader.readtext(image)
    end = time.time()

    inference_time = (end - start) * 1000

    total_time += inference_time
    image_count += 1

    print(f"\nImage: {img_name}")
    print(f"Inference Time: {inference_time:.2f} ms")

    if len(results) > 0:
        detections += 1

    for bbox, text, conf in results:
        print(f"Detected: {text} ({conf:.2f})")


# FINAL SUMMARY


if image_count > 0:
    avg_time = total_time / image_count
    accuracy = (detections / image_count) * 100
else:
    avg_time = 0
    accuracy = 0

print("\n===============================")
print("Evaluation Summary")
print("===============================")
print(f"Images Tested: {image_count}")
print(f"Average Inference Time: {avg_time:.2f} ms")
print(f"Detection Accuracy: {accuracy:.2f}%")