from app.src.config import Settings, settings


def get_app_settings() -> Settings:
    """Get application settings (singleton)."""
    return settings
