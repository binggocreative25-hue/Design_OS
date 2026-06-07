from dataclasses import dataclass


@dataclass
class ClientPipeline:

    client_name: str

    status: str

    next_action: str = ""

    notes_count: int = 0

    project_count: int = 0

    client_score: int = 0

    client_tier: str = "BRONZE"

    def to_dict(self):

        return {
            "client_name":
                self.client_name,

            "status":
                self.status,

            "next_action":
                self.next_action,

            "notes_count":
                self.notes_count,

            "project_count":
                self.project_count,

            "client_score":
                self.client_score,

            "client_tier":
                self.client_tier
        }