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
    decision = llm.get(env.OLLAMA_VISION_MODEL, env.OLLAMA_VISION_DECISION_PROMPT, camera.captured_images())
    logging.info(f"Decided: {decision}")
    print(f"Decided: {decision}")
    return decision

def find(thing, localization=None):
    decision = llm.get(env.OLLAMA_VISION_MODEL, utils.findObjectVisionPrompt(thing, localization), camera.captured_images())
    logging.info(f"Decided: {decision}")
    print(f"Decided: {decision}")
    return decision
