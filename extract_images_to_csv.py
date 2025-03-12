import cv2
import pytesseract
import pandas as pd
import os

# Path to folder containing images
image_folder = "images"  # Change this to your folder path
output_folder = "csv_output"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Path to Tesseract OCR (Update this if installed in a different location)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to process an image and save extracted text as CSV
def process_image(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    # Convert to grayscale for better OCR results
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding (optional, improves accuracy)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Extract text
    text = pytesseract.image_to_string(gray)

    # Convert text into a structured format (modify as needed)
    lines = text.strip().split("\n")
    data = [line.split() for line in lines]

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Get image name without extension
    image_name = os.path.splitext(os.path.basename(image_path))[0]

    # Save CSV with the same name as the image
    csv_path = os.path.join(output_folder, f"{image_name}.csv")
    df.to_csv(csv_path, index=False, header=False)

    print(f"Saved: {csv_path}")

# Process all images in the folder
for filename in os.listdir(image_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        process_image(os.path.join(image_folder, filename))

print("All images processed successfully!")
