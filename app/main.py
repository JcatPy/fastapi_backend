from fastapi import FastAPI
from .database import create_db_and_tables
from .routers import posts, users

app = FastAPI()

# This runs once when the app starts
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# This runs once when the app starts
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(posts.router)
app.include_router(users.router)