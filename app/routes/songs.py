from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_songs():
    return {"message": "songs endpoint working!"}
