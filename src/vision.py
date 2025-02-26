from ollama import Client
from time import sleep
import logging
import camera
import env

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def askOllama(model, image_stream, prompt):
    client = Client(host=env.OLLAMA_HOST)
    try:
        return client.generate(model, prompt, image_stream)
    except Exception as e:
        logging.error(f"An error occurred in askOllama: {str(e)}")
        
def decide(waitTime):
    for frame in camera.captured_images():
        decision = askOllama(env.OLLAMA_LANGUAGE_MODEL, frame, env.OLLAMA_VISION_DECISION_PROMPT)
        logging.info(f"Decided: {decision}")
        yield decision
        sleep(waitTime)
        
# Waiting to make find method, for real object search

