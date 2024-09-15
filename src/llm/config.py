from dotenv import load_dotenv
from os import environ

load_dotenv()


class Config:
    GEMINI_ENDPOINT: str = environ.get("GEMINI_ENDPOINT")
    GEMINI_API_KEY: str = environ.get("GEMINI_API_KEY")


settings = Config()
