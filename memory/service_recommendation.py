from memory.client_manager import (
    ClientManager
)

from memory.client_scoring import (
    ClientScoring
)

from models.service_recommendation import (
    ServiceRecommendation,
    RecommendationItem
)


class ServiceRecommendationEngine:

    def __init__(self):

        self.client_manager = (
            ClientManager()
        )

        self.client_scoring = (
            ClientScoring()
        )

    def recommend(
        self,
        client_name: str
    ):

        intelligence = (
            self.client_manager
            .get_client_intelligence(
                client_name
            )
        )

        if not intelligence:

            return None

        client_score = (
            self.client_scoring
            .calculate_score(
                client_name
            )
        )

        category = (
            intelligence[
                "preferred_category"
            ]
            .lower()
        )

        recommendations = []

        #
        # LOGO
        #

        if category == "logo":

            recommendations.extend([

                RecommendationItem(
                    service="Brand Guideline",
                    score=95,
                    reason="Logo project detected"
                ),

                RecommendationItem(
                    service="Stationery Design",
                    score=90,
                    reason="Brand identity expansion"
                ),

                RecommendationItem(
                    service="Social Media Kit",
                    score=85,
                    reason="Brand activation"
                )
            ])

        #
        # BRANDING
        #

        elif category == "branding":

            recommendations.extend([

                RecommendationItem(
                    service="Company Profile",
                    score=95,
                    reason="Branding client"
                ),

                RecommendationItem(
                    service="Social Media Kit",
                    score=90,
                    reason="Brand consistency"
                ),

                RecommendationItem(
                    service="Packaging Design",
                    score=85,
                    reason="Brand extension"
                )
            ])

        #
        # MARKETING
        #

        elif category == "marketing":

            recommendations.extend([

                RecommendationItem(
                    service="Content Calendar",
                    score=95,
                    reason="Marketing client"
                ),

                RecommendationItem(
                    service="Campaign Strategy",
                    score=90,
                    reason="Marketing growth"
                ),

                RecommendationItem(
                    service="Social Media Kit",
                    score=85,
                    reason="Content support"
                )
            ])

        #
        # DEFAULT
        #

        else:

            recommendations.extend([

                RecommendationItem(
                    service="Brand Guideline",
                    score=80,
                    reason="General recommendation"
                ),

                RecommendationItem(
                    service="Company Profile",
                    score=75,
                    reason="Business growth"
                ),

                RecommendationItem(
                    service="Social Media Kit",
                    score=70,
                    reason="Brand visibility"
                )
            ])

        #
        # CLIENT SCORE BONUS
        #

        if client_score.score >= 75:

            recommendations.append(

                RecommendationItem(
                    service="Premium Brand Consultation",
                    score=95,
                    reason="High value client"
                )

            )

        recommendations.sort(
            key=lambda item: item.score,
            reverse=True
        )

        return ServiceRecommendation(

            client_name=client_name,

            client_score=client_score.score,

            client_tier=client_score.tier,

            recommendations=recommendations
        )