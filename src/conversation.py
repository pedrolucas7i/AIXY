import sttClient
import llm
import tts
import env
import commands
import re


def commonConversations():

    response = None
    # Getting the transcribed speech-to-text data
    stt_data = ' '.join(list(sttClient.multi_segment_generator("end")))  # Joining words to form a sentence

    print(clean_text(stt_data))
    if (clean_text(stt_data) in env.COMMANDS):
        commands.executeCommand(clean_text(stt_data))

    elif (stt_data is not None) and (clean_text(stt_data) not in env.COMMANDS):  # Check if the transcribed text is not empty and is not a command
        # Build the prompt for the language model, incorporating the environment variables
        prompt = (
            f"You are an AI assistant interacting with the user in a focused and efficient manner.\n"
            f"**Your behavior instructions**: "
            f"You must always respond concisely and only provide the information that the user has explicitly requested. "
            f"Avoid giving extra details unless the user asks for them. Be helpful, but never over-explain.\n\n"
            f"Model settings:\n"
            f"- Purpose: {env.PURPOSE}\n"
            f"- Personality: {env.PERSONALITY}\n"
            f"- Language model: {env.OLLAMA_LANGUAGE_MODEL}\n"
            f"- The last thing you said: {response}\n"
            f"The user said: {stt_data.strip()}\n\n\n"
            f"Based on this, provide a concise and relevant response without adding unnecessary details."
        )

        # Calling the language model to get the response using the constructed prompt
        response = llm.get(env.OLLAMA_LANGUAGE_MODEL, prompt)
        
        # If a valid response is received, convert it to speech
        if response:
            tts.speak(response)
        else:
            print("Error: No valid response received from the language model.")

    else:
        print("Error: No speech-to-text data received.")



def clean_text(text):
    # Remove punctuation (.,!?)
    text = re.sub(r'[.,!?]', '', text)
    # Strip spaces at beginning and end
    text = text.strip().lower()

    # If there are more spaces than half of the non-space characters,
    # it means the text was separated letter by letter
    if text.count(' ') > len(text.replace(' ', '')) / 2:
        text = text.replace(' ', '')  # Remove ALL spaces inside
    return text
