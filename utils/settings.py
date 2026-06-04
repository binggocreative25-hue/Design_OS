from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    OPENROUTER_MODEL = os.getenv(
        "OPENROUTER_MODEL",
        "qwen/qwen3-32b:free"
    )

    DATABASE_PATH = os.getenv(
        "DATABASE_PATH",
        "memory/design_os.db"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    DEFAULT_LANGUAGE = os.getenv(
        "DEFAULT_LANGUAGE",
        "id"
    )

    SECONDARY_LANGUAGE = os.getenv(
        "SECONDARY_LANGUAGE",
        "en"
    )

    DEFAULT_LANGUAGE = os.getenv(
    "DEFAULT_LANGUAGE",
    "id"
    )

    SECONDARY_LANGUAGE = os.getenv(
        "SECONDARY_LANGUAGE",
        "en"
    )

settings = Settings()