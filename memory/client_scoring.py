from models.client_score import ClientScore
from memory.client_manager import ClientManager


class ClientScoring:
    def get_client_ranking(self):

        ranking = []

        clients = (
            self.client_manager.get_all_clients()
        )

        for client_name in clients:

            try:

                score = (
                    self.calculate_score(
                        client_name
                    )
                )

                ranking.append(
                    score
                )

            except Exception:

                continue

        ranking.sort(
            key=lambda item: item.score,
            reverse=True
        )

        return ranking
    
    def __init__(self):

        self.client_manager = ClientManager()

    def calculate_score(
        self,
        client_name: str
    ) -> ClientScore:

        client = (
            self.client_manager.get_client(
                client_name
            )
        )

        if not client:

            raise ValueError(
                f"Client {client_name} not found"
            )

        projects = (
            self.client_manager.get_client_projects(
                client_name
            )
        )

        notes = (
            self.client_manager.get_client_notes(
                client_name
            )
        )

        total_projects = len(projects)

        categories = set()

        for project in projects:

            category = project[2]

            if category:

                categories.add(
                    category
                )

        category_count = len(categories)

        relationship_notes = len(notes)

        project_score = (
            self.score_project_count(
                total_projects
            )
        )

        category_score = (
            self.score_category_diversity(
                category_count
            )
        )

        note_score = (
            self.score_relationship_notes(
                relationship_notes
            )
        )

        final_score = (
            project_score
            + category_score
            + note_score
        )

        tier = self.determine_tier(
            final_score
        )

        reasons = self.generate_reasons(
            total_projects,
            category_count,
            relationship_notes
        )

        return ClientScore(
            client_id=0,
            client_name=client_name.upper(),
            score=final_score,
            tier=tier,
            total_projects=total_projects,
            category_count=category_count,
            relationship_notes=relationship_notes,
            reasons=reasons
        )

    def score_project_count(
        self,
        total_projects: int
    ):

        if total_projects >= 10:
            return 40

        if total_projects >= 7:
            return 35

        if total_projects >= 5:
            return 30

        if total_projects >= 3:
            return 20

        if total_projects >= 1:
            return 10

        return 0

    def score_category_diversity(
        self,
        category_count: int
    ):

        if category_count >= 5:
            return 30

        if category_count >= 4:
            return 25

        if category_count >= 3:
            return 20

        if category_count >= 2:
            return 10

        if category_count >= 1:
            return 5

        return 0

    def score_relationship_notes(
        self,
        relationship_notes: int
    ):

        if relationship_notes >= 10:
            return 30

        if relationship_notes >= 7:
            return 25

        if relationship_notes >= 5:
            return 20

        if relationship_notes >= 3:
            return 15

        if relationship_notes >= 1:
            return 10

        return 0

    def determine_tier(
        self,
        score: int
    ):

        if score >= 90:
            return "PLATINUM"

        if score >= 75:
            return "GOLD"

        if score >= 60:
            return "SILVER"

        return "BRONZE"

    def generate_reasons(
        self,
        total_projects: int,
        category_count: int,
        relationship_notes: int
    ):

        reasons = []

        if total_projects >= 5:

            reasons.append(
                "repeat client"
            )

        if category_count >= 3:

            reasons.append(
                "multiple service categories"
            )

        if relationship_notes >= 3:

            reasons.append(
                "active relationship history"
            )

        if not reasons:

            reasons.append(
                "new client"
            )

        return reasons