# camera.py
import cv2
import numpy as np
import io
import threading
import time
from picamera2 import Picamera2

class Camera:
    def __init__(self):
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_still_configuration(main={'size': (512, 384)}))
        self.picam2.start()
        
        self.frame = None
        self.lock = threading.Lock()

        # Start a background thread to continuously capture images
        thread = threading.Thread(target=self.update_frame, daemon=True)
        thread.start()

    def update_frame(self):
        while True:
            image = self.picam2.capture_array()
            rotated = np.rot90(image, 2)
            _, buffer = cv2.imencode(".jpg", rotated)
            with self.lock:
                self.frame = buffer.tobytes()
            time.sleep(0.1)  # Adjust FPS as needed

    def get_frame(self):
        with self.lock:
            return self.frame

    def get_web_stream(self):
        while True:
            frame = self.get_frame()
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            else:
                time.sleep(0.1)
