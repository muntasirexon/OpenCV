import cv2
import numpy as np

def count_objects(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    edges = cv2.Canny(blurred, 50, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    min_area = 100  
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
    

    result = img.copy()
    cv2.drawContours(result, filtered_contours, -1, (0, 255, 0), 2)
    
    count = len(filtered_contours)
    cv2.putText(result, f'Objects: {count}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    

    cv2.imshow('Original', img)
    cv2.imshow('Edges', edges)
    cv2.imshow('Detected Objects', result)
    
    print(f"Number of objects detected: {count}")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return result

def main():
    image_path = 'sample.jpg' 
    result = count_objects(image_path)
    
    cv2.imwrite('detected_objects.jpg', result)

if __name__ == "__main__":
    main() 