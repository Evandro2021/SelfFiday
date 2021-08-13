from fastapi import FastAPI
from pydantic import BaseModel
# importando bibliotecas

app = FastAPI()
@app.get("/evandro")
def raiz():
    return {"rock n roll"}
