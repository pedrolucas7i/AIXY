from ollama import Client
from time import sleep
import logging
import camera
import utils
import llm
import env

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        
def decide():
    for frame in camera.captured_images():
        decision = llm.get(env.OLLAMA_VISION_MODEL, env.OLLAMA_VISION_DECISION_PROMPT, frame)
        logging.info(f"Decided: {decision}")
        yield decision

def find(thing, localization=None):
    for frame in camera.captured_images():
        decision = llm.get(env.OLLAMA_VISION_MODEL, utils.findObjectVisionPrompt(thing, localization), frame)
        logging.info(f"Decided: {decision}")
        yield decision
