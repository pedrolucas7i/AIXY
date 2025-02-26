import io
import time
from picamera import PiCamera

def captured_images():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    time.sleep(2)
    
    stream = io.BytesIO()
    for _ in camera.capture_continuous(stream, format='png'):
        stream.seek(0)
        yield stream
        stream.truncate(0)