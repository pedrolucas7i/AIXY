import asyncio
import os
import uuid
import threading
from queue import Queue
import pygame
from edge_tts import Communicate

# Initialize pygame mixer once
pygame.mixer.init()

VOICE = "en-US-JennyNeural"

# Global queue for speech
tts_queue = Queue()
stop_flag = threading.Event()

def start_tts_worker():
    def tts_loop():
        while not stop_flag.is_set():
            text = tts_queue.get()
            if text is None:
                break  # Graceful exit
            try:
                process_tts(text)
            except Exception as e:
                print(f"[TTS Worker] Error: {e}")
            finally:
                tts_queue.task_done()

    thread = threading.Thread(target=tts_loop, daemon=True)
    thread.start()
    return thread

def speak(text: str):
    if not text.strip():
        print("[TTS] Empty text, skipping...")
        return
    print(f"[TTS] Queued: {text}")
    tts_queue.put(text)

def process_tts(text: str):
    filename = f"output_{uuid.uuid4().hex}.mp3"
    print(f"[TTS] Generating speech for: {text}")

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(generate_tts(text, filename))
        loop.close()
    except Exception as e:
        print(f"[TTS] Generation error: {e}")
        return

    try:
        print("[TTS] Playing audio...")
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        print("[TTS] Playback finished.")
    finally:
        if os.path.exists(filename):
            os.remove(filename)

async def generate_tts(text: str, filename: str):
    communicator = Communicate(text=text, voice=VOICE)
    await communicator.save(filename)

def stop_tts_worker():
    stop_flag.set()
    tts_queue.put(None)  # Force worker to stop
