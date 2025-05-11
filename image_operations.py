import cv2
import numpy as np

def load_and_display_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return
    cv2.imshow('Original Image', img)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)
    
    height, width = img.shape[:2]
    resized = cv2.resize(img, (width//2, height//2))
    cv2.imshow('Resized Image', resized)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image_path = 'sample.jpg' 
    load_and_display_image(image_path)

if __name__ == "__main__":
    main() 