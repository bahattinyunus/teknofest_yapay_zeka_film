import os
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    """System settings and environment variables."""
    
    # Project Settings
    PROJECT_NAME: str = "AI Cinematic Universe"
    VERSION: str = "2.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # API Keys (Placeholders)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    RUNWAY_API_KEY: str = os.getenv("RUNWAY_API_KEY", "")
    ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY", "")
    
    # Output Settings
    OUTPUT_DIR: str = "outputs"
    ASSETS_DIR: str = "assets"
    
    class Config:
        case_sensitive = True

settings = Settings()
