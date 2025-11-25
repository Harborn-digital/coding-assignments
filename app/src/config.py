from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    # Application
    PROJECT_NAME: str = "Clean Architecture FastAPI"
    APP_VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "local"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "mysql+aiomysql://root:secretpassword@localhost:3306/app_db"

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = []

    @property
    def all_cors_origins(self) -> list[str]:
        """Get all CORS origins."""
        return self.BACKEND_CORS_ORIGINS

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
