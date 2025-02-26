import logging
import pyaudio
import pyttsx3
import threading
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def init():
    logging.info("Initializing TTS")
    audio = pyaudio.PyAudio()
    tts = pyttsx3.init("nsss")
    tts.setProperty('rate', tts.getProperty('rate') - 20)
    
def text_to_speech(message):
    
        logging.info(f"Converting message to speech: {message}")
        print('\nTTS:\n', message.strip())

        def play_speech():
            try:
                logging.info("Initializing TTS engine")
                engine = pyttsx3.init()
                
                # Adjust the speech rate (optional)
                rate = engine.getProperty('rate')
                engine.setProperty('rate', rate - 50)  # Decrease the rate by 50 units
                
                # Add a short delay before converting message to speech
                time.sleep(0.5)  # Adjust the delay as needed
                
                logging.info("Converting message to speech")
                engine.say(message)
                engine.runAndWait()
                logging.info("Speech playback completed")
            except Exception as e:
                logging.error(f"An error occurred during speech playback: {str(e)}")

        speech_thread = threading.Thread(target=play_speech)
        speech_thread.start()
