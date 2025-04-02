import os
import tempfile
import wave
from flask import Flask, request, jsonify
import whisper
import torch

app = Flask(__name__)

# Forçar o uso do CPU
device = "cpu"
model = whisper.load_model("medium").to(device)  # Move o modelo para CPU

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["audio"]
    fd, temp_wav = tempfile.mkstemp(suffix=".wav")
    with open(temp_wav, "wb") as f:
        f.write(audio_file.read())
    os.close(fd)

    print("Transcribing...")

    result = model.transcribe(temp_wav)

    os.unlink(temp_wav)

    return jsonify({"text": result.get("text", "").strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
