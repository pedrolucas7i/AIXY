import requests
from playsound import playsound
import env

def speek(text):
    url = env.ChatTTS_HOST
    payload = {"text": text}

    try:
        print(f"Sending text to server: {text}")
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            with open("output_audio.wav", "wb") as audio_file:
                audio_file.write(response.content)
            print("Audio file saved successfully: output_audio.wav")

            play_audio()
        else:
            print(f"Error: {response.status_code}, {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

def play_audio():
    try:
        playsound("output_audio.wav")
        print("Audio played successfully!")
    except Exception as e:
        print(f"An error occurred while playing the audio: {e}")

if __name__ == "__main__":
    text = "Hello, this is a test message."
    speek(text)
