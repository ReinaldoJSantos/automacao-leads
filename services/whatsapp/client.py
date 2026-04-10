import requests

class ZApiClient:

    def __init__(self, instance_id: str, token: str, client_token: str):
        self.instance_id = instance_id
        self.token = token
        self.client_token = client_token

    def send_text(self, phone: str, message: str):
        url = f"https://api.z-api.io/instances/{self.instance_id}/token/{self.token}/send-text"

        headers = {
            "Content-Type": "application/json",
            "client-token": self.client_token
        }

        payload = {
            "phone": phone,
            "message": message
        }

        response = requests.post(url, json=payload, headers=headers)

        print("\n📤 Enviando WhatsApp...")
        print("📡 URL:", url)
        print("📦 Payload:", payload)
        print("📊 Status:", response.status_code)
        print("📄 Response:", response.text)

        return response