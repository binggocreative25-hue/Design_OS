import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SERVICE_FILE = (
    BASE_DIR /
    "config" /
    "service_catalog.json"
)


class PricingEngine:

    def __init__(self):

        with open(
            SERVICE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            self.services = json.load(
                file
            )

    def calculate(
        self,
        service_name: str,
        segment: str = "standard"
    ):

        service = self.services[
            service_name
        ]

        local_price = service[
            "local"
        ]

        international_price = service[
            "international"
        ]

        multiplier = 1.0

        if segment == "premium":

            multiplier = 1.5

        elif segment == "luxury":

            multiplier = 2.5

        local_price = {

            key: int(
                value * multiplier
            )

            for key, value
            in local_price.items()
        }

        international_price = {

            key: int(
                value * multiplier
            )

            for key, value
            in international_price.items()
        }

        target_price = local_price[
            "premium"
        ]

        floor_price = int(
            target_price * 0.85
        )

        ceiling_price = int(
            target_price * 1.5
        )

        complexity_score = 50

        if segment == "premium":

            complexity_score = 80

        elif segment == "luxury":

            complexity_score = 95

        return {

            "service": service_name,

            "market_segment": segment,

            "complexity_score":
                complexity_score,

            "local_price":
                local_price,

            "international_price":
                international_price,

            "recommended_package":
                "PREMIUM",

            "negotiation_floor":
                floor_price,

            "target_price":
                target_price,

            "ceiling_price":
                ceiling_price
        }