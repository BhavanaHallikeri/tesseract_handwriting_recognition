import cv2

def preprocess_image(frame):
    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    _, thresholded_frame = cv2.threshold(gray_frame, 150, 255, cv2.THRESH_BINARY)
    return thresholded_frame
