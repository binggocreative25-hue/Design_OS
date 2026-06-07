from dataclasses import dataclass


@dataclass
class SalesStrategy:

    client_name: str

    client_score: int

    client_tier: str

    closing_probability: int

    revenue_potential: str

    priority: str

    estimated_revenue: int

    recommended_actions: list[str]

    upsell_services: list[str]

    def to_dict(
        self
    ):

        return {

            "client_name":
                self.client_name,

            "client_score":
                self.client_score,

            "client_tier":
                self.client_tier,

            "closing_probability":
                self.closing_probability,

            "revenue_potential":
                self.revenue_potential,

            "priority":
                self.priority,

            "estimated_revenue":
                self.estimated_revenue,

            "recommended_actions":
                self.recommended_actions,

            "upsell_services":
                self.upsell_services
        }