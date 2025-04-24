import logging
import pyttsx3
import threading
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize TTS engine globally
logging.info("Initializing TTS")
engine = pyttsx3.init(driverName='espeak')
engine.setProperty('rate', engine.getProperty('rate') - 20)

def speak(text):
    logging.info(f"Converting message to speech: {message}")
    print('\nTTS:\n', message.strip())

    # Define the speech function that uses the initialized TTS engine
    def play_speech():
        try:
            logging.info("Converting message to speech")  
            engine.setProperty('voice', 'mb-us2')
            engine.say(text)
            engine.runAndWait()  # Wait for speech playback to complete
            logging.info("Speech playback completed")
        except Exception as e:
            logging.error(f"An error occurred during speech playback: {str(e)}")

    # Start the speech in a separate thread
    speech_thread = threading.Thread(target=play_speech)
    speech_thread.start()