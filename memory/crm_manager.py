from models.client_pipeline import (
    ClientPipeline
)

from memory.client_manager import (
    ClientManager
)

from memory.client_scoring import (
    ClientScoring
)


class CRMManager:

    PIPELINE_STAGES = [

        "LEAD",

        "CONTACTED",

        "DISCUSSION",

        "PROPOSAL",

        "NEGOTIATION",

        "WON",

        "LOST"
    ]

    def __init__(self):

        self.client_manager = (
            ClientManager()
        )

        self.client_scoring = (
            ClientScoring()
        )

        self.pipeline = {}

    def create_pipeline(
        self,
        client_name: str,
        status: str = "LEAD"
    ):

        client_name = (
            client_name.upper()
        )

        self.pipeline[
            client_name
        ] = status

        return True

    def update_pipeline(
        self,
        client_name: str,
        status: str
    ):

        client_name = (
            client_name.upper()
        )

        if status not in (
            self.PIPELINE_STAGES
        ):
            return False

        self.pipeline[
            client_name
        ] = status

        return True

    def get_pipeline(
        self,
        client_name: str
    ):

        client_name = (
            client_name.upper()
        )

        status = (
            self.pipeline.get(
                client_name,
                "LEAD"
            )
        )

        notes = (
            self.client_manager
            .get_client_notes(
                client_name
            )
        )

        projects = (
            self.client_manager
            .get_client_projects(
                client_name
            )
        )

        score = (
            self.client_scoring
            .calculate_score(
                client_name
            )
        )

        return ClientPipeline(

            client_name=
                client_name,

            status=
                status,

            next_action=
                self.get_next_action(
                    status
                ),

            notes_count=
                len(notes),

            project_count=
                len(projects),

            client_score=
                score.score,

            client_tier=
                score.tier
        )

    def get_all_pipelines(
        self
    ):

        result = []

        for client_name in (
            self.pipeline.keys()
        ):

            result.append(

                self.get_pipeline(
                    client_name
                )

            )

        return result

    def get_next_action(
        self,
        status: str
    ):

        actions = {

            "LEAD":
                "Initial contact",

            "CONTACTED":
                "Schedule discussion",

            "DISCUSSION":
                "Prepare proposal",

            "PROPOSAL":
                "Follow-up proposal",

            "NEGOTIATION":
                "Close deal",

            "WON":
                "Project onboarding",

            "LOST":
                "Re-engagement"
        }

        return actions.get(
            status,
            "Review client"
        )