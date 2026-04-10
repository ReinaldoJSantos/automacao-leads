import os
from services.whatsapp.client import ZApiClient
from services.whatsapp.service import WhatsAppService
from utils.formatar_numero import formatar_numero


class LeadService:

    def __init__(self):
        client = ZApiClient(
            instance_id=os.getenv("ZAPI_INSTANCE_ID"),
            token=os.getenv("ZAPI_TOKEN"),
            client_token=os.getenv("ZAPI_CLIENT_TOKEN")
        )

        self.whatsapp = WhatsAppService(client)

    def processar_lead(self, lead):
        telefone = formatar_numero(lead.telefone)

        mensagem = self._criar_mensagem(lead.nome)

        self.whatsapp.enviar(telefone, mensagem)