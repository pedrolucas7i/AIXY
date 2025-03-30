import io
import time
import subprocess
import numpy as np
from PIL import Image

def captured_images():
    video_device = "/dev/video0"  # Camera device path
    width, height = 512, 384
    pixel_format = "YUYV"
    buffer_size = width * height * 2  # YUYV uses 2 bytes per pixel
    
    command = [
        "v4l2-ctl", "--device", video_device,
        "--set-fmt-video", f"width={width},height={height},pixelformat={pixel_format}",
        "--stream-mmap", "--stream-count=1"
    ]
    
    while True:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        yuv_image = np.frombuffer(process.stdout, dtype=np.uint8)
        if yuv_image.size != buffer_size:
            continue  # Skip if the captured data is incorrect
        
        yuv_image = yuv_image.reshape((height, width, 2))
        rgb_image = yuv_to_rgb(yuv_image)
        img = Image.fromarray(rgb_image)
        
        stream = io.BytesIO()
        img.save(stream, format='PNG')
        stream.seek(0)
        
        yield stream
        time.sleep(0.1)

def yuv_to_rgb(yuv):
    height, width, _ = yuv.shape
    rgb = np.zeros((height, width, 3), dtype=np.uint8)
    
    Y = yuv[:, :, 0].astype(np.float32)
    U = yuv[:, :, 1].astype(np.float32) - 128
    V = yuv[:, :, 1].astype(np.float32) - 128
    
    C = Y - 16
    D = U
    E = V
    
    R = np.clip((298 * C + 409 * E + 128) / 256, 0, 255)
    G = np.clip((298 * C - 100 * D - 208 * E + 128) / 256, 0, 255)
    B = np.clip((298 * C + 516 * D + 128) / 256, 0, 255)
    
    rgb[:, :, 0] = R.astype(np.uint8)
    rgb[:, :, 1] = G.astype(np.uint8)
    rgb[:, :, 2] = B.astype(np.uint8)
    
    return rgb

if __name__ == "__main__":
    for img_stream in captured_images():
        img = Image.open(img_stream)
        img.show()  # Exibir a imagem sem salvar em arquivo
        time.sleep(1)
