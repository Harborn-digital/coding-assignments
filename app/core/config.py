import os
from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "Interview API"
    environment: str = os.getenv("ENVIRONMENT", "dev")
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    access_token_expire_minutes: int = 60
    debug: bool = os.getenv("DEBUG", "0") == "1"

settings = Settings()
