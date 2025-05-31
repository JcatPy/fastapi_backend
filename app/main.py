from fastapi import FastAPI
from websockets.speedups import apply_mask

from .database import create_db_and_tables
from .routers import posts, users, auth, vote

app = FastAPI()

# This runs once when the app starts
#alembic handles everything
'''@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# This runs once when the app starts
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
'''

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)