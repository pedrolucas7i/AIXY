from ollama import Client
from time import sleep
import logging
from camera import Camera
import utils
import llm
import env

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

camera = Camera()
        
def decide(additionalPrompt=None):
    if additionalPrompt:
        decision = llm.get(env.OLLAMA_VISION_MODEL, env.OLLAMA_VISION_DECISION_PROMPT, camera.get_frame())
    else:
        decision = llm.get(env.OLLAMA_VISION_MODEL, env.OLLAMA_VISION_DECISION_PROMPT, camera.get_frame())
    logging.info(f"Decided: {decision}")
    print(f"Decided: {decision}")
    return decision

def find(thing, localization=None, additionalPrompt=None):
    if additionalPrompt:
        decision = llm.get(env.OLLAMA_VISION_MODEL, utils.findObjectVisionPrompt(thing, localization, additionalPrompt=additionalPrompt), camera.get_frame())
    else:
        decision = llm.get(env.OLLAMA_VISION_MODEL, utils.findObjectVisionPrompt(thing, localization), camera.get_frame())
    logging.info(f"Decided: {decision}")
    print(f"Decided: {decision}")
    return decision
