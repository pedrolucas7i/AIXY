import numpy as np
import sounddevice as sd
import queue
import tempfile
import wave
import requests
import os
import time

# Audio parameters
SAMPLE_RATE = 16000  # Whisper requires 16kHz audio
CHANNELS = 1  # Mono
BLOCK_SIZE = 1024  # Block size for continuous recording
SILENCE_THRESHOLD = 1000  # Adjustable silence detection threshold
SILENCE_TIME = 1.5  # Time (seconds) to confirm silence before processing

# Queue to store recorded audio chunks
audio_queue = queue.Queue()

SERVER_URL = "http://127.0.0.1:5000/transcribe"

def audio_callback(indata, frames, time, status):
    """Callback function that continuously records audio."""
    if status:
        print(status)
    audio_queue.put(indata.copy())

def detect_silence(audio_buffer):
    """Detects when the user stops speaking based on volume level."""
    volume = np.abs(audio_buffer).mean()
    return volume < SILENCE_THRESHOLD

def audio_generator():
    """Generates complete speech segments by detecting silence."""
    buffer = np.array([], dtype=np.int16)
    silence_start_time = None

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=np.int16,
                        blocksize=BLOCK_SIZE, callback=audio_callback):
        while True:
            data = audio_queue.get()
            buffer = np.concatenate((buffer, data.flatten()))

            # Check for silence
            if detect_silence(buffer):
                if silence_start_time is None:
                    silence_start_time = time.time()  # Start silence timer
                elif time.time() - silence_start_time > SILENCE_TIME:
                    if len(buffer) > SAMPLE_RATE * 0.5:  # Ensure at least 0.5s of speech
                        text = send_audio_to_server(buffer)  # Send to server
                        print(f"Received: {text}")  # Show ongoing transcription
                        yield text
                    buffer = np.array([], dtype=np.int16)  # Reset buffer
                    silence_start_time = None  # Reset silence detection
            else:
                silence_start_time = None  # Reset timer if voice is detected

def send_audio_to_server(audio_buffer):
    """Saves recorded audio as a WAV file and sends it to the server for transcription."""
    fd, temp_wav = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    with wave.open(temp_wav, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_buffer.tobytes())
    
    print("Sending audio to server...")
    with open(temp_wav, "rb") as f:
        response = requests.post(SERVER_URL, files={"audio": f})
    os.unlink(temp_wav)  # Remove temporary file after use
    
    if response.status_code == 200:
        user_text = response.json().get("text", "").strip()
        if user_text:
            print(f"Server response: {user_text}")
        return user_text
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return ""

if __name__ == "__main__":
    while True:
        print(list(audio_generator()))