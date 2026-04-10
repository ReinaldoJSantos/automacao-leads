from pydantic import BaseModel, field_validator
class Lead(BaseModel):
    nome: str
    telefone: str
    mensagem: str

@field_validator("mensagem")
def validator_mensagem(cls, v):
    if not v or v.strip() == "":
        raise ValueError("Mensagem não pode ser enviada")
    return v