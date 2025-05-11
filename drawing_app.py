import cv2
import numpy as np

class DrawingApp:
    def __init__(self):
        self.canvas = np.ones((600, 800, 3), dtype=np.uint8) * 255
        self.drawing = False
        self.last_point = None
        self.color = (0, 0, 0) 
        self.brush_size = 5
        
        cv2.namedWindow('Drawing App')
        cv2.setMouseCallback('Drawing App', self.draw)
        
        cv2.createTrackbar('Brush Size', 'Drawing App', 5, 50, self.nothing)
    def nothing(self, x):
        pass
    def draw(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.last_point = (x, y)  
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                cv2.line(self.canvas, self.last_point, (x, y), self.color, self.brush_size)
                self.last_point = (x, y)   
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False      
    def run(self):
        while True:
            self.brush_size = cv2.getTrackbarPos('Brush Size', 'Drawing App')
            
            cv2.imshow('Drawing App', self.canvas) 

            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                self.canvas = np.ones((600, 800, 3), dtype=np.uint8) * 255
            elif key == ord('r'):
                self.color = (0, 0, 255)
            elif key == ord('g'):
                self.color = (0, 255, 0)
            elif key == ord('b'):
                self.color = (255, 0, 0)
            elif key == ord('s'):
                cv2.imwrite('drawing.jpg', self.canvas)
                print("Drawing saved as 'drawing.jpg'")
            elif key == ord('q'):
                break
                
        cv2.destroyAllWindows()

def main():
    app = DrawingApp()
    app.run()

if __name__ == "__main__":
    main() 