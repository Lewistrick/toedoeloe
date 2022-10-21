from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import auth, todos, users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)


@app.get("/")
async def home():
    return {"message": "Hello, world!"}
