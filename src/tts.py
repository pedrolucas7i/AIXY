import asyncio
import os
import uuid
from edge_tts import Communicate
import pygame
import threading

# Initialize the Pygame mixer once
pygame.mixer.init()

# Default voice
VOICE = "en-US-JennyNeural"

def speak(text: str):
    try:
        if not text.strip():
            print("[TTS] Empty text provided, skipping TTS.")
            return

        # Ensure main thread is still alive to avoid shutdown errors
        if not threading.main_thread().is_alive():
            print("[TTS] Main thread is not alive. Aborting TTS playback.")
            return

        print(f"[TTS] Generating speech for: {text}")
        filename = f"output_{uuid.uuid4().hex}.mp3"

        # Generate TTS file
        asyncio.run(generate_tts(text, filename))

        # Play the audio file
        print("[TTS] Playing audio...")
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Wait for playback to finish

        print("[TTS] Playback finished.")

        # Remove temporary audio file
        os.remove(filename)

    except Exception as e:
        print(f"[TTS] Error during TTS playback: {e}")

async def generate_tts(text: str, filename: str):
    communicator = Communicate(text=text, voice=VOICE)
    await communicator.save(filename)