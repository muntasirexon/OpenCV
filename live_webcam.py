import cv2
import numpy as np
from datetime import datetime

class LiveWebcamApp:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open camera")
            return
        cv2.namedWindow('Live Webcam')
        
        self.frame_count = 0
        
    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        edges = cv2.Canny(blurred, 50, 150)
        
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        return edges_bgr
    
    def save_frame(self, frame):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'frame_{timestamp}_{self.frame_count}.jpg'
        cv2.imwrite(filename, frame)
        print(f"Saved frame as {filename}")
        self.frame_count += 1
    
    def run(self):
        print("Press 's' to save a frame, 'q' to quit")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Could not read frame")
                break
            processed = self.process_frame(frame)
            
            cv2.imshow('Original', frame)
            cv2.imshow('Live Webcam', processed)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('s'):
                self.save_frame(processed)
            elif key == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    app = LiveWebcamApp()
    app.run()

if __name__ == "__main__":
    main() 