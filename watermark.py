import cv2
import numpy as np

def create_watermark(image_path, watermark_text="Sample Watermark"):

    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return
    watermarked = img.copy()
    
    height, width = img.shape[:2]
    
    overlay = np.zeros((height, width, 3), dtype=np.uint8)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    color = (255, 255, 255)  
    
    (text_width, text_height), _ = cv2.getTextSize(watermark_text, font, font_scale, thickness)
    
    x = width - text_width - 10
    y = height - 10
    

    cv2.putText(overlay, watermark_text, (x, y), font, font_scale, color, thickness)
    
    mask = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
    
    watermarked = cv2.addWeighted(watermarked, 1, overlay, 0.3, 0)
    
    cv2.imshow('Original Image', img)
    cv2.imshow('Watermarked Image', watermarked)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return watermarked

def main():
    image_path = 'sample.jpg'  
    watermarked_image = create_watermark(image_path, "OpenCV Exercise")
    
    cv2.imwrite('watermarked_sample.jpg', watermarked_image)

if __name__ == "__main__":
    main() 