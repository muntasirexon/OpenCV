import cv2
import numpy as np

def nothing(x):
    pass

def apply_threshold():
    img = cv2.imread('sample.jpg')
    if img is None:
        print("Error: Could not load image")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.namedWindow('Threshold Slider')
    cv2.createTrackbar('Threshold', 'Threshold Slider', 127, 255, nothing)
    cv2.createTrackbar('Max Value', 'Threshold Slider', 255, 255, nothing)
    
    while True:
        thresh = cv2.getTrackbarPos('Threshold', 'Threshold Slider')
        max_val = cv2.getTrackbarPos('Max Value', 'Threshold Slider')
        
        _, binary = cv2.threshold(gray, thresh, max_val, cv2.THRESH_BINARY)
        
        cv2.imshow('Original', gray)
        cv2.imshow('Threshold Slider', binary)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

def main():
    apply_threshold()

if __name__ == "__main__":
    main() 