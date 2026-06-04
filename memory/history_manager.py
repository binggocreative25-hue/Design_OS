from collections import Counter

from memory.database import Database
from memory.semantic_search import SemanticSearch

from utils.settings import settings


class HistoryManager:

    def __init__(self):

        self.db = Database(
            settings.DATABASE_PATH
        )

        self.search = SemanticSearch()

    def save_project(
        self,
        brief,
        result
    ):

        self.db.save_project_history(
            brief=brief,
            workflow=result.workflow,
            project_type=result.project_type,
            client_goal=result.client_goal,
            target_audience=result.target_audience,
            creative_direction=result.creative_direction,
            category=result.category,
            tags=",".join(
                result.tags
            )
        )

    def get_recent_projects(
        self,
        limit=50
    ):

        return self.db.get_recent_projects(
            limit
        )

    def find_project(
        self,
        query: str
    ):

        projects = self.get_recent_projects(
            100
        )

        return self.search.find_best_match(
            query,
            projects
        )

    def get_last_project(
        self
    ):

        projects = (
            self.db.get_recent_projects(
                1
            )
        )

        if not projects:
            return None

        project = projects[0]

        return {
            "brief": project[0],
            "workflow": project[1],
            "project_type": project[2],
            "client_goal": project[3],
            "target_audience": project[4],
            "creative_direction": project[5],
            "category": project[6],
            "tags": project[7],
            "created_at": project[8]
        }

    def get_analytics(
        self
    ):

        projects = self.get_recent_projects(
            1000
        )

        workflow_counter = Counter()
        project_type_counter = Counter()
        category_counter = Counter()

        for project in projects:

            workflow_counter[
                project[1]
            ] += 1

            project_type_counter[
                project[2]
            ] += 1

            category_counter[
                project[6]
            ] += 1

        return {
            "total_projects": len(
                projects
            ),
            "top_workflows": workflow_counter.most_common(
                5
            ),
            "top_project_types": project_type_counter.most_common(
                5
            ),
            "top_categories": category_counter.most_common(
                5
            )
        }