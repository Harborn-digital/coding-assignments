from fastapi import FastAPI
from app.api.v1.routes import users, tasks

app = FastAPI(title="Interview API")

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])
