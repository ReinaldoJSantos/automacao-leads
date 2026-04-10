def formatar_numero(numero: str):
    numero = numero.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    if not numero.startswith("55"):
        numero = "55" + numero

        return numero