import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    USDA_API_KEY: str = os.getenv("USDA_API_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")

settings = Settings()
