# Import the necessary module
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
DEFAULT_LANGUAGE = os.getenv('DEFAULT_LANGUAGE')
FIRST_EN_MESSAGE = os.getenv('FIRST_EN_MESSAGE')
OLLAMA_VISION_MODEL = os.getenv('OLLAMA_VISION_MODEL')
OLLAMA_LANGUAGE_MODEL = os.getenv('OLLAMA_LANGUAGE_MODEL')
WHISPER_MODEL = os.getenv('WHISPER_MODEL')
OLLAMA_VISION_DECISION_PROMPT = os.getenv('OLLAMA_VISION_DECISION_PROMPT')
OLLAMA_HOST = os.getenv('OLLAMA_HOST')