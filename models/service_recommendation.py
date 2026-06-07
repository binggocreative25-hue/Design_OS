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

    confidence_score: int = 0

    upsell_opportunity: bool = False

    cross_sell_opportunity: bool = False

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

            "confidence_score":
                self.confidence_score,

            "upsell_opportunity":
                self.upsell_opportunity,

            "cross_sell_opportunity":
                self.cross_sell_opportunity,

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