import asyncio
import os
import uuid
import subprocess
from edge_tts import Communicate

VOICE = "en-US-JennyNeural"

def speak(text: str):
    try:
        if not text.strip():
            print("[TTS] Empty text, skipping...")
            return

        filename = f"output_{uuid.uuid4().hex}.mp3"
        print(f"[TTS] Generating speech for: {text}")

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

        print(f"[TTS] Playing audio file with ffplay: {filename}")
        subprocess.run(["ffplay", "-nodisp", "-autoexit", filename], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[TTS] Playback finished.")

        os.remove(filename)

    except Exception as e:
        print(f"[TTS] Error: {e}")

async def generate_tts(text: str, filename: str):
    communicator = Communicate(text=text, voice=VOICE)
    await communicator.save(filename)
