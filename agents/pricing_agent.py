from tools.pricing_engine import (
    PricingEngine
)

from models.pricing_output import (
    PricingOutput
)


class PricingAgent:

    def __init__(self):

        self.engine = PricingEngine()

    def detect_segment(
        self,
        client_goal: str,
        target_audience: str
    ):

        text = (
            client_goal +
            " " +
            target_audience
        ).lower()

        luxury_keywords = [

            "luxury",
            "high end",
            "eksklusif",
            "ultra premium"
        ]

        premium_keywords = [

            "premium",
            "menengah atas",
            "kelas atas",
            "elegan"
        ]

        for keyword in luxury_keywords:

            if keyword in text:

                return "luxury"

        for keyword in premium_keywords:

            if keyword in text:

                return "premium"

        return "standard"

    def detect_service(
        self,
        project_type: str
    ):

        text = project_type.lower()

        if "logo" in text:

            return "logo_design"

        if "brand" in text:

            return "brand_identity"

        if "poster" in text:

            return "poster_design"

        return "logo_design"

    def generate_price(
        self,
        project_type: str,
        client_goal: str,
        target_audience: str
    ):

        service = self.detect_service(
            project_type
        )

        segment = self.detect_segment(
            client_goal,
            target_audience
        )

        data = self.engine.calculate(
            service,
            segment
        )

        return PricingOutput(
            **data
        )