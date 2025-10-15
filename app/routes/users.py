from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return {"message": "Users endpoint working!"}

@router.post("/signup")
def signup():
    return {"message": "Signup endpoint will be implemented soon!"}

@router.post("/login")
def login():
    return {"message": "Login endpoint will be implemented soon!"}
