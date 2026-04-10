import requests
import os

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


def enviar_whatsapp(numero: str, mensagem: str):
    try:
        url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

        payload = {
            "phone": numero,
            "message": mensagem
        }

        headers = {
            "Client-Token": CLIENT_TOKEN,
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print("📤 Enviando WhatsApp...")
        print("STATUS:", response.status_code)
        print("RESPOSTA:", response.text)

        if response.status_code != 200:
            raise Exception(f"Erro ao enviar mensagem: {response.text}")

        return response.json()

    except Exception as e:
        print("❌ ERRO WHATSAPP:", str(e))
        return None