from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def chat_ai():
    return {"message": "AI Assistant endpoint working!"}
