import sttClient
import brain
import llm
import tts
import env

def commonConversations():
    stt_data = str(list(sttClient.audio_generator()))
    if stt_data is not None:
        tts.text_to_speech(llm.get(env.OLLAMA_LANGUAGE_MODEL, env.PURPOSE +  env.PERSONALITY + "\nImportant text that have been gived by soomeone that are trying to interact with you: " + stt_data))