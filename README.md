# 📄 Real-Time OCR System using EasyOCR and OpenCV

# 📌 Overview

This project implements a real-time Optical Character Recognition (OCR) system capable of detecting and recognizing text from static images and live camera feeds.

The system combines OpenCV for image processing and EasyOCR for deep learning–based text detection and recognition. It processes images through preprocessing, detection, and recognition stages to extract machine-readable text with bounding boxes and confidence scores.

The framework can be applied to tasks such as:
document analysis
signboard recognition
scene text detection
intelligent monitoring systems


# ⚙️ Technologies Used

| Technology | Purpose                                      |
| ---------- | -------------------------------------------- |
| Python     | Programming language                         |
| OpenCV     | Image processing and camera handling         |
| EasyOCR    | Deep learning text detection and recognition |
| NumPy      | Numerical operations                         |
| Matplotlib | Visualization and analysis                   |


# 🧠 System Architecture

The OCR pipeline follows these stages:
Image / Camera Input
        ↓
Image Preprocessing
        ↓
Text Detection
        ↓
Text Recognition
        ↓
Bounding Box Visualization
        ↓
Result Output


# 📂 Project Structure

image-text-extraction-ocr-main
│
├── experimental_scripts
│   ├── camera_test.py            # Camera testing script
│   ├── clean_ocr_results.py      # OCR text cleaning utility
│   ├── evaluation.py             # OCR evaluation experiments
│   ├── metrics_evaluation.py     # Precision, Recall, F1 calculation
│   └── ocr_clean.txt             # Cleaned OCR output
│
├── images
│   ├── train                     # Training images dataset
│   └── test                      # Test images dataset
│
├── output_images
│   ├── camera_snaps              # Captured camera frames
│   ├── ocr_result                # OCR result images
│   ├── original                  # Original input images
│   ├── plots                     # Accuracy graphs
│   └── preprocessed              # Preprocessed images
│
├── ground_truth.txt              # Ground truth labels for evaluation
│
├── image_test.py                 # Static image OCR testing
├── realtime_ocr.py               # Real-time OCR with camera input
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation


# 🔍 Features

Text detection from static images
Real-time OCR using camera input
Bounding box visualization for detected text
Confidence score output
Image preprocessing pipeline
Performance evaluation metrics


# 🖼 Image Preprocessing

To improve OCR accuracy, the following preprocessing techniques are used:
image resizing
grayscale conversion
noise reduction
contrast enhancement
adaptive thresholding
These steps improve text visibility and detection performance.


# 🔠 Text Detection and Recognition

Text detection and recognition are performed using EasyOCR.

Example output:
Detected: BANK (0.84)
Detected: INDIA (0.79)
Detected: PARKING (1.00)

Each detection includes:
bounding box coordinates
recognized text
confidence score


# 📷 Real-Time OCR

The system supports real-time text detection from camera input.

Keyboard Controls
| Key | Fuction              |
| --- | -------------------- |
| O   | Toggle OCR ON/OFF    |
| S   | Save snapshot        |
| Q   | Quit camera          |

Snapshots are saved in:
output_images/camera_snaps


# 📊 Performance Evaluation

The OCR system was evaluated using 100 scene text images.

| Metric                 | Result     |
| ---------------------- | ---------- |
| Dataset Size           | 100 Images |
| Detection Accuracy     | 92%        |
| Precision              | 0.91       |
| Recall                 | 0.92       |
| F1 Score               | 0.91       |
| Average Inference Time | 176 ms     |


# 📈 Comparison with Traditional OCR

| OCR Method       | Precision | Recall | F1 Score | Inference Time |
| ---------------- | --------- | ------ | -------- | -------------- |
| Tesseract OCR    | 0.84      | 0.82   | 0.83     | 320 ms         |
| Proposed EasyOCR | 0.91      | 0.92   | 0.91     | 176 ms         |

The proposed system shows improved performance in scene text recognition and real-time processing.


# 🚀 Installation

Clone the repository
git clone https://github.com/your-username/real-time-ocr.git

Install dependencies
pip install -r requirements.txt


# ▶️ Running the Project

Static Image OCR
python image_test.py
Real-Time Camera OCR
python realtime_ocr.py


# ⚠ Limitations

The system performance may decrease when:
lighting conditions are poor
images are low resolution
text is blurred
backgrounds are highly complex


# 📌 Applications

document digitization
signboard recognition
intelligent monitoring
assistive technology
automated information extraction


# 📚 References

This project uses concepts from:
EasyOCR deep learning OCR framework
OpenCV image processing techniques
Scene text detection research


# 👩‍💻 Author

Developed as part of a research project on real-time OCR using deep learning and computer vision techniques.
