import logging
import threading
import time
import asyncio
import subprocess
import os
from edge_tts import Communicate

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# TTS voice settings (adjust as needed)
VOICE = "en-US-JennyNeural"

# Function to convert text to speech using edge_tts
def speak(message):
    logging.info(f"Converting message to speech: {message}")
    print('\nTTS:\n', message.strip())  # Print the message for debugging

    # Define the function that generates speech asynchronously and plays it in a thread
    def play_speech():
        try:
            logging.info("Starting speech conversion...")

            # Define the async function that uses edge_tts for speech generation
            async def generate_speech():
                communicator = Communicate(text=message, voice=VOICE)
                # Output file path can be changed as needed
                filename = "output.mp3"
                await communicator.save(filename)
                logging.info(f"Speech generated and saved to {filename}")
                
                # Play the generated file (using 'cvlc' or another player)
                subprocess.run(['cvlc', '--play-and-exit', filename], check=True)
                logging.info("Speech playback completed.")
                
                # Cleanup the file after playback
                if os.path.exists(filename):
                    os.remove(filename)

            # Run the async function inside the thread
            asyncio.run(generate_speech())

        except Exception as e:
            logging.error(f"An error occurred during speech conversion: {str(e)}")

    # Create and start a thread to execute the TTS in the background
    speech_thread = threading.Thread(target=play_speech)
    speech_thread.start()

# Example usage:
if __name__ == "__main__":
    # Test the TTS function
    text_to_speech("Hello, I am AIXY, your autonomous robot!")
    
    # Wait to ensure speech has time to be played
    time.sleep(5)  # Adjust the sleep time as needed to ensure speech plays fully
