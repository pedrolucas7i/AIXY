import logging
import pyttsx3
import threading
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize TTS engine globally
logging.info("Initializing TTS")
tts = pyttsx3.init("mb-us2")
tts.setProperty('rate', tts.getProperty('rate') - 20)

def speech(text):
    logging.info(f"Converting message to speech: {message}")
    print('\nTTS:\n', message.strip())

    # Define the speech function that uses the initialized TTS engine
    def play_speech():
        try:
            logging.info("Converting message to speech")
            
            # Adjust the speech rate (optional)
            rate = tts.getProperty('rate')
            
            # Add a short delay before converting message to speech
            time.sleep(0.5)  # Adjust the delay as needed
            
            tts.say(text)
            tts.runAndWait()  # Wait for speech playback to complete
            logging.info("Speech playback completed")
        except Exception as e:
            logging.error(f"An error occurred during speech playback: {str(e)}")

    # Start the speech in a separate thread
    speech_thread = threading.Thread(target=play_speech)
    speech_thread.start()