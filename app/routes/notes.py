from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_notes():
    return {"message": "notes endpoint working!"}
