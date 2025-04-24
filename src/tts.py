import asyncio
import os
import uuid
from edge_tts import Communicate
import pygame
import threading

# Initialize pygame mixer just once
pygame.mixer.init()

VOICE = "en-US-JennyNeural"

# Shared lock to prevent overlapping calls
audio_lock = threading.Lock()

def speak(text: str):
    try:
        if not text.strip():
            print("[TTS] Empty text, skipping...")
            return

        # Prevent overlapping playback with lock
        with audio_lock:
            filename = f"output_{uuid.uuid4().hex}.mp3"
            print(f"[TTS] Generating speech for: {text}")

            # Generate TTS
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

            if loop.is_running():
                coro = generate_tts(text, filename)
                asyncio.run_coroutine_threadsafe(coro, loop).result()
            else:
                loop.run_until_complete(generate_tts(text, filename))

            # Play with pygame
            print("[TTS] Playing audio...")
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            print("[TTS] Playback finished.")
            os.remove(filename)

    except Exception as e:
        print(f"[TTS] Error: {e}")

async def generate_tts(text: str, filename: str):
    communicator = Communicate(text=text, voice=VOICE)
    await communicator.save(filename)
