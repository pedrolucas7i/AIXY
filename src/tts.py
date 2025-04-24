import logging
import asyncio
import edge_tts
import os
import pygame

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Voice settings
VOICE_ID = "en-US-JennyNeural"  # Soft, young adult female voice
RATE = "+5%"  # Slightly faster speech rate

async def generate_and_play(text):
    try:
        logging.info("Generating speech with edge-tts")
        communicate = edge_tts.Communicate(text, voice=VOICE_ID, rate=RATE)
        output_file = "output.mp3"
        await communicate.save(output_file)
        logging.info(f"Audio saved as {output_file}, now playing")

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(1)

        # Clean up after playback
        os.remove(output_file)
        logging.info("Audio playback finished and file deleted.")

    except Exception as e:
        logging.error(f"An error occurred during speech playback: {str(e)}")


def speak(text):
    logging.info(f"Converting message to speech: {text}")
    print('\nTTS:\n', text.strip())

    # Run the speech generation and playback using asyncio in the main thread
    asyncio.run(generate_and_play(text))