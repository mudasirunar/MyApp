from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_games():
    return {"message": "games endpoint working!"}
