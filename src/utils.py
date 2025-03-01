from ollama import Client
from time import sleep
import logging
import json
import env

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def accessMemory(thing, category):
    if category is 'info':
        pass
    elif category is 'visual':
        pass
    else:
        logging.warning("Invalid Category!")
    
def addMemory(thing, definition, category):
    pass

    """
    MEMORY FILE (SQLITE DATABASE)
    Example:
    ------------------------------------------------
    |   thing   |   definition   |     category    |
    ------------------------------------------------
    
    categories = [info, visual]
    """

def makePrompt(model, toDo, thing, color=None, localization=None, MemoryFile=True):
    logging.info("Making Prompt")
    definition = None
    
    if toDo is 'find':
        category = 'visual'
    elif toDo is 'search':
        category = 'info'
    else:
        logging.warning("Invalid toDo! Changing category to 'info'...")
        print("Invalid toDo! Changing toDo to 'search' and category to 'info'...")
        toDo = 'search'
        category = 'info'
    
    if MemoryFile:
        definition = accessMemory(thing, category)
    
    if definition is None:
        if category is 'info':
            data = {'thing': thing, "color": color, "localization": localization}
            return env.OLLAMA_EN_SEARCH_PROMPT + f'{json.dumps(data)}'
        elif category is 'visual':
            data = f"Your main objective is to detect the '{thing}' object and approach it, when you find it you must come face to face with it, with a distance between you of 100mm, in this case you should ignore all other outputs and only provide the word 'finded', without additional explanations."
            if color is not None and localization is not None:
                data = f"Your main objective is to detect the '{thing}' object with the '{color}' color in the '{localization}' localization and approach it, when you find it you must come face to face with it, with a distance between you of 100mm, in this case you should ignore all other outputs and only provide the word 'finded', without additional explanations."
            elif color is not None and localization is None:
                data = f"Your main objective is to detect the '{thing}' object with the '{color}' color and approach it, when you find it you must come face to face with it, with a distance between you of 100mm, in this case you should ignore all other outputs and only provide the word 'finded', without additional explanations."
            elif color is None and localization is not None:
                data = f"Your main objective is to detect the '{thing}' object in the '{localization}' localization and approach it, when you find it you must come face to face with it, with a distance between you of 100mm, in this case you should ignore all other outputs and only provide the word 'finded', without additional explanations."
            return env.OLLAMA_VISION_DECISION_PROMPT + data