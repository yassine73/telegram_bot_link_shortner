import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    API_BASE_URL: str = os.getenv("API_BASE_URL", "http://localhost:8000")
    STATIC_HELP_MSG: str = "Please send me your LINK so i can make it shortner!"
    LINK_REGEX: str = r'\bhttps?:\/\/[^\s<>"]+|www\.[^\s<>"]+'

settings = Settings()