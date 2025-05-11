import cv2
import numpy as np
from datetime import datetime

def process_video():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'recorded_video_{timestamp}.avi'
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
    
    print("Recording started. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        
        cv2.imshow('Original', frame)
        cv2.imshow('Grayscale', gray_bgr)
        
        out.write(gray_bgr)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved as {output_file}")

def main():
    process_video()

if __name__ == "__main__":
    main() 