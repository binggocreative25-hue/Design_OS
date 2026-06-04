import json
from pathlib import Path

from models.project_context import (
    ProjectContext
)

BASE_DIR = Path(__file__).resolve().parent.parent

CONTEXT_FILE = (
    BASE_DIR /
    "memory" /
    "project_context.json"
)


class ContextManager:

    def save(
        self,
        context: ProjectContext
    ):

        with open(
            CONTEXT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                context.model_dump(),
                file,
                ensure_ascii=False,
                indent=4
            )

    def load(
        self
    ):

        if not CONTEXT_FILE.exists():

            return None

        with open(
            CONTEXT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

        return ProjectContext(
            **data
        )

    def save_project_context(
        self,
        context: ProjectContext
    ):

        self.save(
            context
        )

    def load_project_context(
        self
    ):

        return self.load()