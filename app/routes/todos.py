from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_todos():
    return {"message": "Todos endpoint working!"}
