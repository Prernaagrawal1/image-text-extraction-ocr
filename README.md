# image-text-extraction-ocr
Text extraction from images and real-time camera using EasyOCR
# Text Extraction from Images using Pattern Recognition

## Overview
This project implements a **text extraction (OCR) system** using **EasyOCR** to recognize text from both **static images** and **real-time camera input**. The system is designed to demonstrate practical OCR workflows along with basic performance evaluation and visualization.

This project is developed as a **final-year major project**.

---

## Features
- Text extraction from image datasets (train and test)
- Manual ground truth creation for evaluation
- Character-level accuracy calculation
- Visual analysis of OCR performance
- Real-time camera-based OCR
- Snapshot capture from live OCR

---

## Technologies Used
- Python  
- EasyOCR  
- OpenCV  
- Matplotlib  
- Anaconda (Conda environment)
  
## Project Structure
image-text-extraction-ocr/
├── project.py
├── camera_test.py
├── README.md
├── requirements.txt
├── ocr_results.txt
├── ground_truth.txt
│
├─── images/
│ ├── train/
│ └── test/
│
└─── output_images/
  ├── ocr_result/
  ├── plots/
  └── camera_snaps/

---

## Evaluation Method
- OCR is performed on all images in the dataset.
- Ground truth is manually created for **50 selected images**.
- Accuracy is calculated by comparing OCR output with ground truth.
- Performance is analyzed using visual plots and annotated images.

---

## ▶️ How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run OCR on images
python project.py

3️⃣ Run live camera OCR
python camera_test.py

--- 

📈 Results
Accurate text extraction from printed images
Real-time recognition using webcam
Performance visualized through plots and annotated images

---


🔮 Future Scope
Support for multilingual OCR (Hindi + English)
Deploy as web application using Streamlit
Improve accuracy using deep learning-based OCR models
