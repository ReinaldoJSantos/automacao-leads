from dotenv import load_dotenv
import os
from services.whatsapp.client import ZApiClient

load_dotenv()

# ⚠️ Se não estiver usando .env carregado automaticamente

print("INSTANCE_ID:", os.getenv("ZAPI_INSTANCE_ID"))
print("TOKEN:", os.getenv("ZAPI_TOKEN"))
print("CLIENT_TOKEN:", os.getenv("ZAPI_CLIENT_TOKEN"))

client = ZApiClient(
    instance_id=os.getenv("ZAPI_INSTANCE_ID"),
    token=os.getenv("ZAPI_TOKEN"),
    client_token=os.getenv("ZAPI_CLIENT_TOKEN")
)

response = client.send_text(
    "5571992930117",  # coloca seu número aqui
    "Teste envio 🚀"
)

print("Resposta final:", response.text)