import requests

INSTANCE_ID = "3F16681384EE2182B1E6BA4D31290A14"
TOKEN = "DB4EA406686150A044AAB287"
CLIENT_TOKEN = "F19804a2e124146e58ba0e9169c63d22fS"

def enviar_whatsapp(numero, mensagem):
    url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

    payload = {
        "phone": numero,
        "message": mensagem
    }

    headers = {
        "Client-Token": CLIENT_TOKEN,
        "Content-Type": "application/json"
    }

    print("URL:", url)
    print("PAYLOAD:", payload)

    response = requests.post(url, json=payload, headers=headers)

    print(response.status_code)
    print(response.text)


enviar_whatsapp("5571992930117", "🚀 Teste WhatsApp")