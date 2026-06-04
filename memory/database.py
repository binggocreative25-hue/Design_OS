from pathlib import Path
import sqlite3
from datetime import datetime


DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT,
    project_type TEXT,
    status TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT,
    country TEXT,
    industry TEXT,
    notes TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS project_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brief TEXT NOT NULL,
    workflow TEXT,
    project_type TEXT,
    client_goal TEXT,
    target_audience TEXT,
    creative_direction TEXT,
    category TEXT,
    tags TEXT,
    created_at TEXT NOT NULL
);
"""


class Database:

    def __init__(self, db_path: str):

        self.db_path = db_path

        db_folder = Path(db_path).parent

        db_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        self.connection = sqlite3.connect(
            db_path,
            check_same_thread=False
        )

        self.connection.executescript(
            DB_SCHEMA
        )

        self._ensure_phase_1i_columns()

        self.connection.commit()

    def _ensure_phase_1i_columns(self):

        cursor = self.connection.cursor()

        cursor.execute(
            "PRAGMA table_info(project_history)"
        )

        columns = [
            row[1]
            for row in cursor.fetchall()
        ]

        if "category" not in columns:

            cursor.execute(
                """
                ALTER TABLE project_history
                ADD COLUMN category TEXT
                """
            )

        if "tags" not in columns:

            cursor.execute(
                """
                ALTER TABLE project_history
                ADD COLUMN tags TEXT
                """
            )

        self.connection.commit()

    def save_interaction(
        self,
        role: str,
        content: str
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO interactions
            (
                role,
                content,
                created_at
            )
            VALUES
            (
                ?,
                ?,
                ?
            )
            """,
            (
                role,
                content,
                datetime.utcnow().isoformat()
            )
        )

        self.connection.commit()

    def get_recent_interactions(
        self,
        limit: int = 20
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT role, content
            FROM interactions
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        rows = cursor.fetchall()

        rows.reverse()

        return rows

    def create_client(
        self,
        client_name: str,
        country: str,
        industry: str,
        notes: str = ""
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO clients
            (
                client_name,
                country,
                industry,
                notes,
                created_at
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                client_name,
                country,
                industry,
                notes,
                datetime.utcnow().isoformat()
            )
        )

        self.connection.commit()

    def create_project(
        self,
        project_name: str,
        project_type: str,
        status: str
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO projects
            (
                project_name,
                project_type,
                status,
                created_at
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                project_name,
                project_type,
                status,
                datetime.utcnow().isoformat()
            )
        )

        self.connection.commit()

    def save_project_history(
        self,
        brief: str,
        workflow: str,
        project_type: str,
        client_goal: str,
        target_audience: str,
        creative_direction: str,
        category: str,
        tags: str
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO project_history
            (
                brief,
                workflow,
                project_type,
                client_goal,
                target_audience,
                creative_direction,
                category,
                tags,
                created_at
            )
            VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """,
            (
                brief,
                workflow,
                project_type,
                client_goal,
                target_audience,
                creative_direction,
                category,
                tags,
                datetime.utcnow().isoformat()
            )
        )

        self.connection.commit()

    def get_recent_projects(
        self,
        limit: int = 20
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT
                brief,
                workflow,
                project_type,
                client_goal,
                target_audience,
                creative_direction,
                category,
                tags,
                created_at
            FROM project_history
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        return cursor.fetchall()

    def close(self):

        self.connection.close()