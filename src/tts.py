import logging
import threading
import asyncio
import edge_tts
from playsound import playsound
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Voice settings
VOICE_ID = "en-US-JennyNeural"  # Soft, young adult female voice
RATE = "+5%"  # Slightly faster speech rate

def speak(text):
    logging.info(f"Converting message to speech: {text}")
    print('\nTTS:\n', text.strip())

    async def generate_and_play():
        try:
            logging.info("Generating speech with edge-tts")
            communicate = edge_tts.Communicate(text, voice=VOICE_ID, rate=RATE)
            await communicate.save("output.mp3")
            logging.info("Audio saved, waiting briefly before playback")
            await asyncio.sleep(0.5)  # Ensure file is ready
            playsound("output.mp3")
            logging.info("Playback complete")
        except Exception as e:
            logging.error(f"An error occurred during speech playback: {str(e)}")

    def threaded_play():
        asyncio.run(generate_and_play())

    # Run the speech generation and playback in a separate thread
    speech_thread = threading.Thread(target=threaded_play)
    speech_thread.start()
