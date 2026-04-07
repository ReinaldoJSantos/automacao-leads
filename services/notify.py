import requests

TOKEN = "8278294916:AAFKGASveuERib-g_MYnLvzcpoD-vxw-erA"
CHAT_ID = "8435801353"

def enviar_notificacao(nome, telefone, mensagem):
    texto = f"""
🚀 Novo Lead!

👤 Nome: {nome}
📞 Telefone: {telefone}
💬 Mensagem: {mensagem}
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": texto
    }

    requests.post(url, data=payload)



# print("🚀 Iniciando teste...")

# TOKEN = "8278294916:AAFKGASveuERib-g_MYnLvzcpoD-vxw-erA"
# CHAT_ID = "8435801353"

# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# payload = {
#     "chat_id": CHAT_ID,
#     "text": "Teste direto 🚀"
# }

# response = requests.post(url, data=payload)

# print("Status:", response.status_code)
# print("Resposta:", response.text)