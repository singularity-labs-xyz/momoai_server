from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/")
def getUsers():
    return {"message": "users"}