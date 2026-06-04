from pydantic import BaseModel


class ProjectContext(BaseModel):

    project_type: str

    client_goal: str

    target_audience: str

    creative_direction: str

    workflow: str