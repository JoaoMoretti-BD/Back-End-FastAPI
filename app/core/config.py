from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "API - Mercearia do João"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./mercearia.db"
    SECRET_KEY: str = "sua-chave-super-secreta-aqui-mude-em-producao"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
