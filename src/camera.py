import base64
import threading
import time
import subprocess
from ollama import Client

# Configuração do servidor
client = Client(host='http://82.155.114.161:11430')

def capture_image():
    """Captura uma imagem usando fswebcam e retorna o caminho da imagem."""
    image_path = "image.jpg"
    try:
        subprocess.run(["fswebcam", "-q", image_path], check=True)
        return image_path
    except subprocess.CalledProcessError:
        print("Erro: Falha ao capturar imagem com fswebcam.")
        return None

def encode_image(image_path):
    """Codifica a imagem capturada em Base64."""
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string
    except Exception as e:
        print(f"Erro ao codificar a imagem: {e}")
        return None

def process_images():
    """Captura e processa imagens continuamente em segundo plano."""
    while True:
        image_path = capture_image()
        if image_path:
            encoded_image = encode_image(image_path)
            if encoded_image:
                try:
                    response = client.generate(
                        model='llava-llama3',
                        prompt='What is in this picture?',
                        images=[encoded_image]
                    )

                    print(response)

                    print(f"\n\n{response.get('response', 'Nenhuma resposta disponível')}\n")

                except Exception as e:
                    print(f"Erro ao processar a imagem: {e}")

        time.sleep(10)  # Aguarda 10 segundos antes da próxima captura

# Inicia a thread de captura sem bloquear o programa principal
try:
    thread = threading.Thread(target=process_images, daemon=True)
    thread.start()
except Exception as e:
    print(f"Erro ao iniciar a thread: {e}")

# Mantém o programa rodando
while True:
    time.sleep(1)
