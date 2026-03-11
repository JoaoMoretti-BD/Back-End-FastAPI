#pip install pydantic_settings
from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME:str="API - Mercearia"
    VERSION:str="1.0"
    DATABASE_URL:str="sqlite:///./mercearia.db"
    SECRET_KEY:str="sua chave secreta"
    ALGORITH:str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 30

settings = Settings()