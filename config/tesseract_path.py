import pytesseract

def set_tesseract_path():
    # Set the path for Tesseract (if necessary)
    # Update the path based on your installation
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
