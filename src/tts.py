import asyncio
import os
import uuid
import threading
import subprocess
from queue import Queue, Empty
from edge_tts import Communicate

VOICE = "en-US-JennyNeural"
tts_queue = Queue()
stop_flag = threading.Event()

def start_tts_worker():
    def tts_loop():
        while not stop_flag.is_set():
            try:
                text = tts_queue.get(timeout=1)
                if text is None:
                    break
                process_tts(text)
            except Empty:
                continue
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
    if stop_flag.is_set():
        print("[TTS] Skipping due to shutdown.")
        return

    filename = f"output_{uuid.uuid4().hex}.mp3"
    print(f"[TTS] Generating: {text}")

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(generate_tts(text, filename))
        loop.close()
    except Exception as e:
        print(f"[TTS] Error generating: {e}")
        return

    try:
        print(f"[TTS] Playing with ffplay: {filename}")
        subprocess.run(
            ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", filename]
        )
        print("[TTS] Done.")
    finally:
        if os.path.exists(filename):
            os.remove(filename)

async def generate_tts(text: str, filename: str):
    communicator = Communicate(text=text, voice=VOICE)
    await communicator.save(filename)

def stop_tts_worker():
    print("[TTS] Stopping...")
    stop_flag.set()
    tts_queue.put(None)
