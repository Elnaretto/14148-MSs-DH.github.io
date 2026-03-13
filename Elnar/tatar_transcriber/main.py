from PIL import Image, ImageOps, ImageEnhance
import cv2
import numpy as np
import pytesseract
from normalize import clean_text, normalize_arabic
from transliterate import transliterate, latin_to_cyrillic

# -----------------------------
# 1. Improved image preprocessing for OCR
# -----------------------------
def preprocess_image(file_path):
    """
    Convert image to black-and-white, enhance contrast, denoise for better OCR
    """
    image = Image.open(file_path)
    gray = ImageOps.grayscale(image)

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(2.0)

    # Resize to improve OCR recognition
    gray = gray.resize((gray.width*2, gray.height*2))

    # Convert to numpy array for OpenCV
    img_np = np.array(gray)

    # Median filter to remove noise
    img_np = cv2.medianBlur(img_np, 3)

    # Binarization (thresholding)
    _, img_np = cv2.threshold(img_np, 140, 255, cv2.THRESH_BINARY)

    processed = Image.fromarray(img_np)
    return processed

# -----------------------------
# 2. OCR recognition
# -----------------------------
processed_image = preprocess_image("test2.png")
ocr_text = pytesseract.image_to_string(processed_image, lang="ara", config="--psm 6")

# -----------------------------
# 3. Clean and normalize OCR text
# -----------------------------
clean_image = clean_text(ocr_text)
norm_image = normalize_arabic(clean_image)

# -----------------------------
# 4. Transcription (Latin)
# -----------------------------
latin_image = transliterate(norm_image)

# -----------------------------
# 5. Convert to Cyrillic
# -----------------------------
cyrillic_image = latin_to_cyrillic(latin_image)

# -----------------------------
# 6. Save results
# -----------------------------
with open("output_image.txt", "w", encoding="utf-8") as f:
    f.write("=== RAW OCR ===\n")
    f.write(ocr_text + "\n\n")
    f.write("=== Transcription (Latin) ===\n")
    f.write(latin_image + "\n\n")
    f.write("=== Tatar Cyrillic ===\n")
    f.write(cyrillic_image + "\n")

# -----------------------------
# 7. Print results for quick check
# -----------------------------
print("=== RAW OCR ===")
print(ocr_text[:500])
print("\n=== Transcription (Latin) ===")
print(latin_image[:500])
print("\n=== Tatar Cyrillic ===")
print(cyrillic_image[:500])
