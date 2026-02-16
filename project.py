import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import cv2
import easyocr
import matplotlib.pyplot as plt

# ===============================
# INITIALIZE OCR
# ===============================
reader = easyocr.Reader(['en'], gpu=False)

# ===============================
# LIVE CAMERA OCR (BEST VERSION)
# ===============================
print("\n--- Advanced Live Camera OCR ---")
print("Controls:")
print("O -> Toggle OCR ON/OFF")
print("S -> Save Snapshot")
print("Q -> Quit")

os.makedirs("output_images/camera_snaps", exist_ok=True)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("ERROR: Camera not accessible")
    sys.exit()

ocr_enabled = True
frame_count = 0
ocr_results = []
stable_text = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # ========= BEST UNIVERSAL OCR PREPROCESSING =========

    # Resize (huge accuracy boost)
    frame_resized = cv2.resize(
        frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC
    )

    # Convert to LAB (best for colored text)
    lab = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Enhance contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l = clahe.apply(l)

    lab = cv2.merge((l, a, b))
    enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    # Adaptive threshold version
    gray = cv2.cvtColor(enhanced, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    # ========= OCR (run every 15 frames) =========
    if ocr_enabled and frame_count % 15 == 0:
        try:
            ocr_color = reader.readtext(enhanced)
            ocr_thresh = reader.readtext(thresh)
            ocr_results = ocr_color + ocr_thresh
        except:
            ocr_results = []

    # ========= STABILIZE TEXT =========
    stable_text.clear()
    for bbox, text, conf in ocr_results:
        if conf < 0.6:
            continue
        stable_text[text] = max(conf, stable_text.get(text, 0))

    # ========= DRAW RESULTS =========
    for text, conf in stable_text.items():
        for bbox, t, _ in ocr_results:
            if t == text:
                (tl, tr, br, bl) = bbox
                tl = tuple(map(int, tl))
                br = tuple(map(int, br))

                cv2.rectangle(frame_resized, tl, br, (0, 255, 0), 2)
                cv2.putText(
                    frame_resized,
                    f"{text} ({conf:.2f})",
                    (tl[0], tl[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )
                break

    # ========= INSTRUCTIONS =========
    cv2.putText(
        frame_resized,
        "O: OCR ON/OFF | S: Save | Q: Quit",
        (10, frame_resized.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow("Advanced Live OCR", frame_resized)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('o'):
        ocr_enabled = not ocr_enabled
        ocr_results = []
        print(f"OCR Enabled: {ocr_enabled}")
    elif key == ord('s'):
        snap_name = f"output_images/camera_snaps/snap_{frame_count}.png"
        cv2.imwrite(snap_name, frame_resized)
        print(f"Snapshot saved: {snap_name}")

# ===============================
# CLEAN EXIT
# ===============================
cap.release()
cv2.destroyAllWindows()
print("Advanced Camera OCR Stopped.")