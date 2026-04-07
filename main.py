from fastapi import FastAPI
from pydantic import BaseModel
from services.sheets import salvar_lead
from services.notify import enviar_notificacao

app = FastAPI()

class Lead(BaseModel):
    nome: str
    telefone: str
    mensagem: str

# @app.post("/lead")
# async def criar_lead(lead: Lead):
#     print(f"Novo lead criado com sucesso: {lead}")
#     return {"status": "ok"}

@app.post("/lead")
def receber_lead(lead: Lead):
    salvar_lead(lead.nome, lead.telefone, lead.mensagem)
    enviar_notificacao(lead.nome, lead.telefone, lead.mensagem)
    return {"mensagem": "Lead salvo e notificado!"}

