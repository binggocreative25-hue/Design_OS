from dataclasses import dataclass, field
from typing import List


@dataclass
class RecommendationItem:

    service: str
    score: int
    reason: str


@dataclass
class ServiceRecommendation:

    client_name: str

    client_score: int
    client_tier: str

    recommendations: List[
        RecommendationItem
    ] = field(
        default_factory=list
    )

    def to_dict(self):

        return {
            "client_name":
                self.client_name,

            "client_score":
                self.client_score,

            "client_tier":
                self.client_tier,

            "recommendations": [

                {
                    "service":
                        item.service,

                    "score":
                        item.score,

                    "reason":
                        item.reason
                }

                for item
                in self.recommendations
            ]
        }