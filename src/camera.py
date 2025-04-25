import cv2
import numpy as np
import io
from PIL import Image
import time
from picamera2 import Picamera2

def captured_images():
    with Picamera2() as picam2:
        picam2.configure(picam2.create_still_configuration(main={'size': (512, 384)}))
        picam2.start()
        frame = picam2.capture_array()
        rotated = np.rot90(frame, 2)
        return convertToBytes(rotated)
        
def convertToBytes(image_array):
    """Convert NumPy image array to bytes."""
    _, buffer = cv2.imencode(".jpg", image_array)
    return io.BytesIO(buffer).read()

def getWebStream():
    while True:
        yield (b'--frame\r\n'   
                b'Content-Type: image/jpeg\r\n\r\n' + captured_images() + b'\r\n')
