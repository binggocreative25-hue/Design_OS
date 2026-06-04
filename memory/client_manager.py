import re
from collections import Counter
from datetime import datetime

from memory.database import Database

from utils.settings import settings


class ClientManager:

    def __init__(self):

        self.db = Database(
            settings.DATABASE_PATH
        )

    def extract_client_name(
        self,
        brief: str
    ):

        patterns = [

            r"perusahaan\s+([A-Za-z0-9_-]+)",

            r"client\s+([A-Za-z0-9_-]+)",

            r"klien\s+([A-Za-z0-9_-]+)"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                brief,
                re.IGNORECASE
            )

            if match:

                return match.group(
                    1
                ).upper()

        return None

    def save_client_if_needed(
        self,
        brief: str
    ):

        client_name = (
            self.extract_client_name(
                brief
            )
        )

        if not client_name:

            return None

        cursor = (
            self.db.connection.cursor()
        )

        cursor.execute(
            """
            SELECT id
            FROM clients
            WHERE client_name = ?
            """,
            (client_name,)
        )

        existing = (
            cursor.fetchone()
        )

        if existing:

            return client_name

        self.db.create_client(
            client_name=client_name,
            country="Unknown",
            industry="Unknown",
            notes="Auto Generated"
        )

        return client_name

    def get_client(
        self,
        client_name: str
    ):

        cursor = (
            self.db.connection.cursor()
        )

        cursor.execute(
            """
            SELECT
                client_name,
                country,
                industry,
                notes
            FROM clients
            WHERE client_name = ?
            """,
            (
                client_name.upper(),
            )
        )

        return cursor.fetchone()

    def get_client_projects(
        self,
        client_name: str
    ):

        cursor = (
            self.db.connection.cursor()
        )

        keyword = (
            client_name.upper()
        )

        cursor.execute(
            """
            SELECT
                brief,
                workflow,
                category,
                tags,
                created_at
            FROM project_history
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        projects = []

        for row in rows:

            brief = row[0]

            if keyword in brief.upper():

                projects.append(
                    row
                )

        return projects

    #
    # PHASE 2C
    #

    def get_client_intelligence(
        self,
        client_name: str
    ):

        projects = (
            self.get_client_projects(
                client_name
            )
        )

        if not projects:

            return None

        workflow_counter = Counter()

        category_counter = Counter()

        tag_counter = Counter()

        dates = []

        unique_briefs = set()

        for project in projects:

            workflow = project[1]
            category = project[2]
            tags = project[3]
            created_at = project[4]

            unique_briefs.add(
                project[0]
            )

            if workflow:
                workflow_counter[
                    workflow
                ] += 1

            if category:
                category_counter[
                    category
                ] += 1

            if tags:

                for tag in tags.split(","):

                    tag = tag.strip()

                    if tag:

                        tag_counter[
                            tag
                        ] += 1

            if created_at:
                dates.append(
                    created_at
                )

        return {

            "total_projects":
                len(projects),

            "unique_projects":
                len(unique_briefs),

            "preferred_category":
                category_counter.most_common(
                    1
                )[0][0]
                if category_counter
                else "-",

            "most_used_workflow":
                workflow_counter.most_common(
                    1
                )[0][0]
                if workflow_counter
                else "-",

            "top_tags":
                [
                    tag
                    for tag, _
                    in tag_counter.most_common(
                        10
                    )
                ],

            "first_seen":
                min(dates)
                if dates
                else "-",

            "last_seen":
                max(dates)
                if dates
                else "-"
        }

    #
    # PHASE 2D
    # CLIENT RECOMMENDATION ENGINE
    #

    def recommend_services(
        self,
        client_name: str
    ):

        intelligence = (
            self.get_client_intelligence(
                client_name
            )
        )

        if not intelligence:

            return None

        category = (
            intelligence[
                "preferred_category"
            ]
            .lower()
        )

        recommendations = []

        if category == "branding":

            recommendations = [

                (
                    "Brand Guideline",
                    95
                ),

                (
                    "Company Profile",
                    90
                ),

                (
                    "Social Media Kit",
                    88
                )
            ]

        elif category == "marketing":

            recommendations = [

                (
                    "Content Calendar",
                    94
                ),

                (
                    "Campaign Strategy",
                    90
                ),

                (
                    "Social Media Kit",
                    85
                )
            ]

        elif category == "logo":

            recommendations = [

                (
                    "Brand Guideline",
                    95
                ),

                (
                    "Stationery Design",
                    88
                ),

                (
                    "Social Media Kit",
                    85
                )
            ]

        else:

            recommendations = [

                (
                    "Brand Guideline",
                    80
                ),

                (
                    "Company Profile",
                    75
                ),

                (
                    "Social Media Kit",
                    70
                )
            ]

        return {

            "category":
                category,

            "upsell_score":
                recommendations[0][1],

            "recommendations":
                recommendations
        }
    
    #
    # PHASE 2E
    # CLIENT RELATIONSHIP MEMORY
    #

    def add_client_note(
        self,
        client_name: str,
        note: str
    ):

        cursor = (
            self.db.connection.cursor()
        )

        cursor.execute(
            """
            INSERT INTO client_notes (
                client_name,
                note,
                created_at
            )
            VALUES (?, ?, ?)
            """,
            (
                client_name.upper(),
                note,
                datetime.now().isoformat()
            )
        )

        self.db.connection.commit()

    def get_client_notes(
        self,
        client_name: str
    ):

        cursor = (
            self.db.connection.cursor()
        )

        cursor.execute(
            """
            SELECT
                note,
                created_at
            FROM client_notes
            WHERE client_name = ?
            ORDER BY id DESC
            """,
            (
                client_name.upper(),
            )
        )

        return cursor.fetchall()