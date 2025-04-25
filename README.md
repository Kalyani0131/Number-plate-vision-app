# **Number-Plate-Vision-App** 📸🚗

This Project is a web-based application built with Streamlit, designed to automatically detect and extract text from vehicle number plates. This project leverages advanced computer vision techniques to process images and uses Optical Character Recognition (OCR) to identify the license plate text. It is ideal for automating tasks such as vehicle identification, parking management, and security monitoring.

## Key Features

- **License Plate Detection**: Detects and highlights license plates from vehicle images using contour detection.Automatically identifies regions that resemble license plates and draws bounding boxes around them.
- **Optical Character Recognition (OCR)**: Extracts license plate numbers from detected regions using Tesseract OCR.Provides the recognized license plate number in text format.
- **Dynamic Image Processing**: Canny edge detection with adjustable thresholds allows fine-tuning for optimal detection results.Processes images to enhance edges and detect contours, improving plate detection accuracy.
- **Downloadable Outputs**: Allows users to download the processed image with detected plates and the extracted license plate number as a text file.

---

## Prerequisites

Before running this project, ensure you have the following:

-  Python 3.x
-   Required Python Libraries:
    - **Tesseract OCR
    - **OpenCV
    - **Streamlit
- Streamlit installed for the front-end interface

## Installation

### Step 1: Install Required Libraries

Install the necessary libraries using pip:

```bash
pip install streamlit opencv-python numpy pillow pytesseract
```

## Usage

Upload an Image:
- Upload an image in JPG, PNG, or JPEG format.
Adjust Canny Edge Detection Parameters (Optional):
- Low Threshold: The minimum intensity gradient to detect edges.
- High Threshold: The maximum intensity gradient for edge detection.
Dark Mode (Optional):
- Enable Dark Mode by checking the box. This will change the background color of the app to dark mode for easier viewing in low-light environments.
License Plate Detection and Extraction:
- Edge detection: The app converts the image to grayscale and applies a bilateral filter to improve the edges.
- Contour detection: It uses contours to find the license plate in the image.
- OCR (Optical Character Recognition): The app then uses Tesseract OCR to extract the text from the detected license plate.

## Running the Application
To run the application locally, open a terminal and execute the following command:
```
streamlit run app.py
```
Replace app.py with the name of your Streamlit Python file.

## Screenshot
![Screenshot 2024-12-09 154415](https://github.com/user-attachments/assets/59af7a2e-d9d6-4ca9-b18d-49de23e32338)
![Screenshot 2024-12-09 154551](https://github.com/user-attachments/assets/b430421f-6fd0-4d9d-92b2-3830e7d6db5b)








