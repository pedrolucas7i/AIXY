import asyncio
import aiohttp
from playsound import playsound
import threading
import env

async def speek(text):
    # URL of the AI server endpoint
    url = env.ChatTTS_HOST
    
    # Prepare the JSON payload
    payload = {"text": text}

    try:
        print(f"Sending text to server: {text}")
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                # Check if the response is successful
                if response.status == 200:
                    audio_data = await response.read()

                    # Save the received audio file
                    with open("output_audio.wav", "wb") as audio_file:
                        audio_file.write(audio_data)
                    print("Audio file saved successfully: output_audio.wav")

                    # Run the function to play audio after saving it
                    await asyncio.to_thread(play_audio)

                else:
                    print(f"Error: {response.status}, {await response.text()}")

    except Exception as e:
        print(f"An error occurred: {e}")

def play_audio():
    try:
        playsound("output_audio.wav")
        print("Audio played successfully!")
    except Exception as e:
        print(f"An error occurred while playing the audio: {e}")

# You can run the asyncio loop to call text_to_speech:
if __name__ == "__main__":
    text = "Hello, this is a test message."
    asyncio.run(text_to_speech(text))
