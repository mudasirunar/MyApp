from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from app.routes import users, todos, reminders, notes, games, songs, university, ai_assistant

app = FastAPI(title="MyApp Backend", version="1.0")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # (later limit to your desktop & android app)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(todos.router, prefix="/todos", tags=["Todos"])
app.include_router(reminders.router, prefix="/reminders", tags=["Reminders"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])
app.include_router(games.router, prefix="/games", tags=["Games"])
app.include_router(songs.router, prefix="/songs", tags=["Songs"])
app.include_router(university.router, prefix="/university", tags=["University"])
app.include_router(ai_assistant.router, prefix="/ai", tags=["AI Assistant"])

@app.get("/")
def root():
    return {"message": "Welcome to MyApp Backend 🚀"}

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Backend is alive!"}
