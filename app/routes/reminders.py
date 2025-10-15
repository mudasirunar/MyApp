from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_reminders():
    return {"message": "reminders endpoint working!"}
