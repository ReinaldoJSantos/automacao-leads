import os
import json
import gspread
from google.oauth2.service_account import Credentials

def salvar_lead(nome, telefone, mensagem):
    # Defina as credenciais do Google Sheets
    scopes = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"
            ]
    creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

    client = gspread.authorize(creds)

    planilha = client.open("Automacao Leads").sheet1
    planilha.append_row([nome, telefone, mensagem])
    print("Lead salvo com sucesso!")
