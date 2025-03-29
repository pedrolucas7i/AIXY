import io
import time
from picamera2 import Picamera2

def captured_images():
    stream = io.BytesIO()
    for _ in picam2.capture_continuous(stream, format='png'):
        stream.seek(0)
        yield stream
        stream.truncate(0)

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration(main={'size': (512, 384)}))
picam2.start()
