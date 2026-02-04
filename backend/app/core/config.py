from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Platform API"
    ENV: str = "development"

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Database
    DATABASE_URL: str

    # CORS
    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        env_file = ".env"
        extra = "ignore"  # IMPORTANT safety net


settings = Settings()
