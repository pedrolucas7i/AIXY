import whisper
import numpy as np
import sounddevice as sd
import queue
import tempfile
import threading
import wave
import os
import time

# Load Whisper model (Use 'tiny' for better Raspberry Pi performance)
model = whisper.load_model('base')

# Audio parameters
SAMPLE_RATE = 16000         # Whisper requires 16kHz audio
CHANNELS = 1                # Mono audio
BLOCK_SIZE = 1024           # Block size for continuous recording
SILENCE_THRESHOLD = 500     # Silence detection threshold (adjustable)
SILENCE_TIME = 1.5          # Time in seconds to confirm silence

# Queue for storing recorded audio chunks
audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    """Callback function that continuously records audio."""
    if status:
        print(status)
    audio_queue.put(indata.copy())

def detect_silence(audio_buffer):
    """Detects when the user stops speaking based on volume level."""
    volume = np.abs(audio_buffer).mean()
    return volume < SILENCE_THRESHOLD

def record_audio():
    """Continuously records audio and detects when the user stops speaking."""
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
                    silence_start_time = time.time()                    # Start silence timer
                elif time.time() - silence_start_time > SILENCE_TIME:
                    if len(buffer) > SAMPLE_RATE * 0.5:                 # Ensure at least 0.5s of speech
                        process_audio(buffer)                           # Send only when speaking is finished
                    buffer = np.array([], dtype=np.int16)               # Reset buffer
                    silence_start_time = None                           # Reset silence detection
            else:
                silence_start_time = None                               # Reset timer if voice is detected

def process_audio(audio_buffer):
    """Transcribes the recorded speech and returns"""
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

    with wave.open(temp_wav.name, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_buffer.tobytes())

    print("Transcribing...")
    result = model.transcribe(audio=temp_wav.name)
    user_text = result.get("text", "").strip()
    print(f"You said: {user_text}")

    if user_text:
        yield user_text

# Start recording in a separate thread
recording_thread = threading.Thread(target=record_audio, daemon=True)
recording_thread.start()