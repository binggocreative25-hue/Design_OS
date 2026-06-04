from pydantic import BaseModel


class PricingOutput(BaseModel):

    service: str

    market_segment: str

    complexity_score: int

    local_price: dict

    international_price: dict

    recommended_package: str

    negotiation_floor: int

    target_price: int

    ceiling_price: int