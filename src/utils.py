from ollama import Client
from time import sleep
import logging
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
    
def addMemory(thing, definition):
    pass

def makePrompt(model, toDo, thing, color=None, localization=None, MemoryFile=True):
    logging.info("Making Prompt")
    
    if toDo is 'find':
        category = 'visual'
    elif toDo is 'search':
        category = 'info'
    else:
        logging.warning("Invalid toDo! Changing category to 'info'...")
        print("Invalid toDo! Changing category to 'info'...")
        category = 'info'
    
    
    definition = accessMemory(thing, category)    
    
    
    """
    PROMPT
    
    toDo:           find
    thing:          computer
    color:          None
    localization:   None
    """
    
    """
    MEMORY FILE (SQLITE DATABASE)
    Example:
    ------------------------------------------------
    |   thing   |   definition   |     category    |
    ------------------------------------------------
    
    categories = [info, visual]
    """