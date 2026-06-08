from memory.client_scoring import (
    ClientScoring
)

from memory.service_recommendation import (
    ServiceRecommendationEngine
)

from memory.crm_manager import (
    CRMManager
)

from models.sales_strategy import (
    SalesStrategy
)


class SalesManager:

    def __init__(
        self
    ):

        self.client_scoring = (
            ClientScoring()
        )

        self.service_engine = (
            ServiceRecommendationEngine()
        )

        self.crm_manager = (
            CRMManager()
        )

    def generate_strategy(
        self,
        client_name: str
    ):

        score = (
            self.client_scoring
            .calculate_score(
                client_name
            )
        )

        services = (
            self.service_engine
            .recommend(
                client_name
            )
        )

        pipeline = (
            self.crm_manager
            .get_pipeline(
                client_name
            )
        )

        closing_probability = (
            self.calculate_probability(
                score.score
            )
        )

        revenue_potential = (
            self.calculate_revenue_level(
                score.score
            )
        )

        priority = (
            self.calculate_priority(
                score.score
            )
        )

        estimated_revenue = (
            self.calculate_revenue(
                score.score
            )
        )

        recommended_actions = (
            self.get_actions(
                pipeline.status
            )
        )

        upsell_services = [

            item.service

            for item in
            services.recommendations[:2]
        ]

        return SalesStrategy(

            client_name=client_name,

            client_score=score.score,

            client_tier=score.tier,

            closing_probability=
            closing_probability,

            revenue_potential=
            revenue_potential,

            priority=
            priority,

            estimated_revenue=
            estimated_revenue,

            recommended_actions=
            recommended_actions,

            upsell_services=
            upsell_services
        )

    def get_leaderboard(
        self
    ):

        leaderboard = []

        clients = (
            self.crm_manager
            .pipeline
            .keys()
        )

        for client in clients:

            try:

                strategy = (
                    self.generate_strategy(
                        client
                    )
                )

                leaderboard.append(
                    strategy
                )

            except Exception:

                continue

        leaderboard.sort(

            key=lambda item: (

                item.closing_probability,

                item.estimated_revenue

            ),

            reverse=True
        )

        return leaderboard

    def get_pipeline_analytics(
        self
    ):

        leaderboard = (
            self.get_leaderboard()
        )

        total_revenue = sum(
            item.estimated_revenue
            for item in leaderboard
        )

        forecast_revenue = sum(

            int(
                item.estimated_revenue
                *
                (
                    item.closing_probability
                    / 100
                )
            )

            for item in leaderboard
        )

        high_priority = len(

            [
                item
                for item in leaderboard
                if item.priority == "A"
            ]
        )

        return {

            "total_pipeline":
                total_revenue,

            "forecast_revenue":
                forecast_revenue,

            "high_priority":
                high_priority,

            "opportunities":
                len(leaderboard)

        }

    def calculate_probability(
        self,
        score
    ):

        return min(
            95,
            score + 20
        )

    def calculate_revenue_level(
        self,
        score
    ):

        if score >= 80:
            return "HIGH"

        if score >= 60:
            return "MEDIUM"

        return "LOW"

    def calculate_priority(
        self,
        score
    ):

        if score >= 80:
            return "A"

        if score >= 60:
            return "B"

        return "C"

    def calculate_revenue(
        self,
        score
    ):

        return (
            score * 100000
        )

    def get_actions(
        self,
        status
    ):

        actions = {

            "LEAD": [
                "Initial contact"
            ],

            "CONTACTED": [
                "Schedule meeting"
            ],

            "DISCUSSION": [
                "Prepare proposal"
            ],

            "PROPOSAL": [
                "Follow-up proposal"
            ],

            "NEGOTIATION": [
                "Close deal"
            ],

            "WON": [
                "Project onboarding"
            ],

            "LOST": [
                "Re-engagement"
            ]
        }

        return actions.get(
            status,
            ["Review client"]
        )        