import sttClient
import brain
import llm
import tts
import env

def commonConversations():
    tts.text_to_speech(llm.get(env.OLLAMA_LANGUAGE_MODEL, env.PURPOSE + env.PERSONALITY + list(sttClient.audio_generator())))