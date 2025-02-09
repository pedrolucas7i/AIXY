from ollama import Client
import base64

# Função para codificar a imagem em base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

# Configuração do servidor (verifique se o IP está correto)
client = Client(host='http://192.168.1.47:11430')

# Codifica a imagem para base64
image_path = 'image.jpg'  # Substitua pelo caminho da sua imagem
encoded_image = encode_image(image_path)

# Envia a mensagem e a imagem codificada para o modelo llava-llama3
response = client.generate(
    model='llava-llama3',  # Modelo configurado no servidor
    prompt='What is in this picture?',
    images=[encoded_image]  # A imagem codificada em base64
)

# Exibe a resposta completa para inspeção
print(response)

# Tente acessar a chave certa para a resposta
try:
    print(f"\n\n{response['response']}\n")
except KeyError:
    print("A chave 'message' não existe. Estrutura da resposta:", response)
