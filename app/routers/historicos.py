from fastapi import APIRouter

router = APIRouter(
    prefix="/historicos",
    tags=["Historicos"],
    responses={404: {"description": "Not Found"}},
)

@router.get("/")
async def get_historicos():
    return {"message": "Rota para lista completa dos históricos de todas ações"}
