import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\kalyani\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Set up page config
st.set_page_config(page_title="Number Plate Vision App", page_icon="🚗", layout="centered")

# Add background image with CSS
def add_bg_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://img.freepik.com/free-vector/abstract-digital-grid-vector-black-background_53876-111550.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stButton button:hover {
            background-color: #ff6347;
            color: white;
        }
        .stImage {
            border: 5px solid #ddd;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        </style>
        """, unsafe_allow_html=True
    )

add_bg_image()

# App title
st.title("Number Plate Vision App 🚗")

# Image uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Slider for Canny edge detection parameters
low_threshold = st.slider("Canny Low Threshold", min_value=0, max_value=100, value=30)
high_threshold = st.slider("Canny High Threshold", min_value=100, max_value=300, value=200)

# Add dark mode toggle
dark_mode = st.checkbox("Enable Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        .stApp {background-color: #1e1e1e; color: white;}
        </style>
        """, unsafe_allow_html=True
    )

if uploaded_file:
    # Show loading spinner
    with st.spinner('Processing your image...'):
        # Convert image
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert to grayscale and apply bilateral filter
        gray_image = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)

        # Apply Canny edge detection with slider values
        edged = cv2.Canny(gray_image, low_threshold, high_threshold)

        # Show processed images
        st.subheader("Processed Images")
        st.image(gray_image, caption="Grayscale Image", use_container_width=True, channels="GRAY")
        st.image(edged, caption="Edged Image", use_container_width=True, channels="GRAY")

        # Find contours
        cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
        screenCnt = None

        for c in cnts:
            perimeter = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
            if len(approx) == 4:
                screenCnt = approx
                x, y, w, h = cv2.boundingRect(c)
                new_img = img_array[y:y+h, x:x+w]
                st.image(new_img, caption="Detected License Plate", use_container_width=True)
                break

        # Check if license plate was detected
        if screenCnt is not None:
            # Draw contours and save the image with detected plate
            cv2.drawContours(img_array, [screenCnt], -1, (0, 255, 0), 3)
            output_file = "detected_plate.png"
            cv2.imwrite(output_file, img_array)  # Save the processed image

            # Display the image with detected plate
            st.image(img_array, caption="Image with Detected License Plate", use_container_width=True)

            # Extract license plate text using OCR
            license_text = pytesseract.image_to_string(new_img)
            st.write(f"License Plate Number: {license_text.strip()}")

            # Allow the user to download the processed image
            with open(output_file, "rb") as file:
                st.download_button(label="Download Processed Image", data=file, file_name=output_file, mime="image/png")

            # Allow the user to download the extracted license plate text
            with open("license_plate.txt", "w") as f:
                f.write(license_text.strip())
            with open("license_plate.txt", "rb") as file:
                st.download_button("Download License Plate Number", data=file, file_name="license_plate.txt", mime="text/plain")

        else:
            st.warning("No license plate detected. Please try another image.")
