import logging
import asyncio
import edge_tts
import os
import pygame

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

VOICE_ID = "en-US-JennyNeural"
RATE = "+5%"
OUTPUT_FILE = "output.mp3"

# Initialize Pygame mixer
pygame.mixer.init()

# Use this to prevent reuse after interpreter shutdown
_loop = None
_shutdown = False


async def _generate_tts(text):
    logging.info("Generating speech with edge-tts")
    communicate = edge_tts.Communicate(text, voice=VOICE_ID, rate=RATE)
    await communicate.save(OUTPUT_FILE)
    logging.info(f"Audio saved as {OUTPUT_FILE}, now playing")

    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    os.remove(OUTPUT_FILE)
    logging.info("Audio playback finished and file deleted.")


def speak(text: str):
    global _loop, _shutdown

    if _shutdown:
        logging.error("TTS system is shut down, cannot schedule new tasks.")
        return

    logging.info(f"Converting message to speech: {text}")
    print("\nTTS:\n", text.strip())

    try:
        if _loop is None or _loop.is_closed():
            _loop = asyncio.new_event_loop()
            asyncio.set_event_loop(_loop)

        asyncio.run_coroutine_threadsafe(_generate_tts(text), _loop)

    except RuntimeError as e:
        logging.error(f"Runtime error during speech playback: {str(e)}")
    except Exception as e:
        logging.error(f"General error during speech playback: {str(e)}")


def shutdown_tts():
    global _loop, _shutdown
    _shutdown = True
    if _loop and not _loop.is_closed():
        _loop.call_soon_threadsafe(_loop.stop)
        _loop.close()
        logging.info("TTS loop successfully shut down.")
