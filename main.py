from fastapi import FastAPI
from pydantic import BaseModel
from services.sheets import salvar_lead
from services.notify import enviar_notificacao
from fastapi.middleware.cors import CORSMiddleware
from services.whatsapp import enviar_whatsapp

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois podemos restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Lead(BaseModel):
    nome: str
    telefone: str
    mensagem: str


@app.post("/lead")
def receber_lead(lead: Lead):
    print("Recebido", lead)

    salvar_lead(lead.nome, lead.telefone, lead.mensagem)
    enviar_notificacao(lead.nome, lead.telefone, lead.mensagem)

    # NOVO 🔥
    enviar_whatsapp(
        lead.telefone,
        f"Olá {lead.nome}, recebemos seu contato! Em breve vamos te atender."
)

    return {"mensagem": "Lead salvo e notificado!"}


@app.get("/")
def home():
    return {"mensagem": "API de automação rodando 🚀"}