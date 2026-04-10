import os
from dotenv import load_dotenv
from services.whatsapp.client import ZApiClient
from services.whatsapp.service import WhatsAppService
from utils.formatar_numero import formatar_numero

load_dotenv()


class LeadService:

    def __init__(self):
        client = ZApiClient(
            instance_id=os.getenv("ZAPI_INSTANCE_ID"),
            token=os.getenv("ZAPI_TOKEN"),
            client_token=os.getenv("ZAPI_CLIENT_TOKEN")
        )

        self.whatsapp = WhatsAppService(client)

        
    def _validar_mensagem(self, mensagem: str):
        if not mensagem or mensagem.strip() == "":
            raise ValueError("Mensagem não pode ser vazia")

    def processar_lead(self, lead):
        telefone = formatar_numero(lead.telefone)

        mensagem = self._criar_mensagem(lead.nome)
        try:

            self.whatsapp.enviar(telefone, mensagem)
        except Exception as e:
            print("Erro ao enviar WhatsApp", e)

        return {"mensagem": "Lead processado com sucesso"}
        print(f"📩 Lead enviado: {lead.nome} - {telefone}")

    def _criar_mensagem(self, nome):

        return (
    f"Olá {nome}! 👋 Recebi seu contato e já vou te ajudar.\n\n"
    "Me conta rapidinho:\n"
    "👉 Qual sua principal necessidade hoje?\n\n"
    "Assim já te direciono melhor 😉"
)
