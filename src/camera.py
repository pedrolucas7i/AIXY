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
        return convertToBytes(picam2.capture_array())
        
def convertToBytes(image_array):
    """Convert NumPy image array to bytes."""
    _, buffer = cv2.imencode(".jpg", image_array)
    return io.BytesIO(buffer).read()

def getWebStream():
    with Picamera2() as picam2:
        picam2.configure(picam2.create_still_configuration(main={'size': (512, 384)}))
        picam2.start()
        return (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + convertToBytes(picam2.capture_array()) + b'\r\n')
