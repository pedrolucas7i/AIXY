import io
import time
from picamera import PiCamera


def captured_images():
    stream = io.BytesIO()
    for _ in camera.capture_continuous(stream, format='png'):
        stream.seek(0)
        yield stream
        stream.truncate(0)
   
        
camera = PiCamera()
camera.resolution = (512,384)