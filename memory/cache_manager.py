import json
import hashlib

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

CACHE_DIR = (
    BASE_DIR /
    "memory" /
    "cache"
)

CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


class CacheManager:

    def make_key(
        self,
        prompt: str
    ) -> str:

        return hashlib.md5(
            prompt.encode(
                "utf-8"
            )
        ).hexdigest()

    def get(
        self,
        prompt: str
    ):

        key = self.make_key(
            prompt
        )

        cache_file = (
            CACHE_DIR /
            f"{key}.json"
        )

        if not cache_file.exists():

            return None

        with open(
            cache_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    def save(
        self,
        prompt: str,
        response: str
    ):

        key = self.make_key(
            prompt
        )

        cache_file = (
            CACHE_DIR /
            f"{key}.json"
        )

        with open(
            cache_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {
                    "response": response
                },
                file,
                ensure_ascii=False,
                indent=4
            )