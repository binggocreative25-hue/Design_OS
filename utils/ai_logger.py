from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_FILE = (
    BASE_DIR /
    "logs" /
    "ai_calls.log"
)


class AILogger:

    @staticmethod
    def log(
        agent: str,
        provider: str,
        status: str
    ):

        timestamp = (
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        line = (
            f"[{timestamp}] "
            f"{agent} | "
            f"{provider} | "
            f"{status}\n"
        )

        with open(
            LOG_FILE,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                line
            )