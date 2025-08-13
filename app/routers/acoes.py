from fastapi import APIRouter

router = APIRouter(
    prefix="/acoes",
    tags=["Acoes"],
    responses={404: {"description": "Not Found"}},
)

@router.get("/")
async def get_acoes():
    return {"message": "Rota para lista completa de ações"}
