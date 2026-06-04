from pydantic import BaseModel
from pydantic import field_validator


class DirectorOutput(BaseModel):

    project_type: str

    client_goal: str

    target_audience: str

    creative_direction: str

    workflow: str

    category: str = ""

    tags: list[str] = []

    @field_validator(
        "workflow",
        mode="before"
    )
    @classmethod
    def validate_workflow(
        cls,
        value
    ):

        if isinstance(
            value,
            list
        ):

            return value[-1]

        return str(value)