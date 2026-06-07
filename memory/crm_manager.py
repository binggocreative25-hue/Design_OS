import json
from pathlib import Path

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

        self.storage_file = (
            Path(
                "memory/crm_pipeline.json"
            )
        )

        self.pipeline = (
            self.load_pipeline()
        )

    def load_pipeline(
        self
    ):

        if not (
            self.storage_file.exists()
        ):

            return {}

        try:

            with open(
                self.storage_file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(
                    file
                )

        except Exception:

            return {}

    def save_pipeline(
        self
    ):

        with open(
            self.storage_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.pipeline,
                file,
                indent=4
            )

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
        
        self.save_pipeline()
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
        
        self.save_pipeline()
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

    def get_dashboard_summary(
        self
    ):

        summary = {}

        for stage in (
            self.PIPELINE_STAGES
        ):

            summary[
                stage
            ] = 0

        for status in (
            self.pipeline.values()
        ):

            if status in summary:

                summary[
                    status
                ] += 1

        return summary

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