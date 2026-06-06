from dataclasses import dataclass, field
from typing import List


@dataclass
class ClientScore:
    client_id: int
    client_name: str

    score: int = 0
    tier: str = "BRONZE"

    total_projects: int = 0
    category_count: int = 0
    relationship_notes: int = 0

    reasons: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "client_id": self.client_id,
            "client_name": self.client_name,
            "score": self.score,
            "tier": self.tier,
            "total_projects": self.total_projects,
            "category_count": self.category_count,
            "relationship_notes": self.relationship_notes,
            "reasons": self.reasons,
        }