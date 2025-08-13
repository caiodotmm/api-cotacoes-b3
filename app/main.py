from fastapi import FastAPI
from routers import acoes, historicos

app = FastAPI()

app.include_router(acoes.router)
app.include_router(historicos.router)

@app.get("/")
def read_root():
    return {"message": "API Cotações B3 rodando"}
 
