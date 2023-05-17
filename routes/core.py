from fastapi import APIRouter
from main import chain_manager
from main import document_manager


router = APIRouter(prefix="/core")

@router.get("/llm/{inp}", response_model=None)
def llm(inp: str):
    return {"message": chain_manager.default_chains["llm"].run(inp)}