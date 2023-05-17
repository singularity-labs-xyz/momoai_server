from fastapi import APIRouter
from momoai_core import managers
from momoai_core import chains

chain_manager = managers.ChainManager()
document_manager = managers.DocumentManager()

router = APIRouter(prefix="/core")

@router.get("/")
def users():
    return {"message": "core"}


@router.get("/upload")
def upload():
    pass

@router.get("/llm/{inp}")
def llm(inp: str):
    return chain_manager.default_chains["llm"].run(inp)