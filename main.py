from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.post("/comprar")
def comprar_titulo(
    telefone: str, 
    email: str, 
    cpf: str, 
    quantidade: int, 
    credentials: HTTPBasicCredentials = Depends(security)
):
    # Verificação de autenticação
    if credentials.username != "admin" or credentials.password != "12345":
        raise HTTPException(status_code=401, detail="Autenticação falhou")
    
    return {"status": "OK", "mensagem": "Compra registrada com sucesso"}

