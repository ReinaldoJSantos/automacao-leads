class WhatsAppService:

    def __init__(self, client):
        self.client = client

    def enviar(self, telefone: str, mensagem: str):
        self._validar(telefone, mensagem)

        response = self.client.send_text(telefone, mensagem)

        if response.status_code not in [200, 201]:
            raise Exception(
        f"Erro ao enviar WhatsApp: {response.status_code} - {response.text}"
    )

        return response.json()

    def _validar(self, telefone, mensagem):
        if not telefone:
            raise ValueError("Telefone é obrigatório")

        if not mensagem or mensagem.strip() == "":
            raise ValueError("Mensagem não pode ser vazia")