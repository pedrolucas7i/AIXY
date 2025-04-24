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

# Initialize the event loop globally (to avoid creating it multiple times)
loop = asyncio.get_event_loop()

# Function to generate and play speech asynchronously
async def generate_and_play(text):
    try:
        logging.info("Generating speech with edge-tts")
        communicate = edge_tts.Communicate(text, voice=VOICE_ID, rate=RATE)
        output_file = "output.mp3"
        await communicate.save(output_file)
        logging.info(f"Audio saved as {output_file}, now playing")

        # Initialize pygame mixer for audio playback (ensure pygame is initialized each time)
        pygame.mixer.quit()  # Quit any previous mixer instance
        pygame.mixer.init()  # Reinitialize the mixer for each execution

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


# Public function to call from outside the module
def speak(text):
    logging.info(f"Converting message to speech: {text}")
    print('\nTTS:\n', text.strip())

    # Ensure we're using the existing event loop
    loop.run_until_complete(generate_and_play(text))

# Optional: If you want to run this module directly, you can test it like this:
# if __name__ == "__main__":
#     speak("Hello! This is a test message.")
