from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_university():
    return {"message": "university endpoint working!"}
