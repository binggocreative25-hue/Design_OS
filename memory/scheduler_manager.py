import json
from pathlib import Path


class SchedulerManager:

    def __init__(self):

        self.file_path = (
            Path(__file__).parent /
            "scheduler_tasks.json"
        )

        if not self.file_path.exists():

            self.file_path.write_text(
                "[]",
                encoding="utf-8"
            )

    def _load_tasks(self):

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def _save_tasks(
        self,
        tasks
    ):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                tasks,
                file,
                indent=4
            )

    def create_task(
        self,
        title,
        date
    ):

        tasks = self._load_tasks()

        task = {
            "id": (
                len(tasks) + 1
            ),
            "title": title,
            "date": date,
            "status": "PENDING"
        }

        tasks.append(
            task
        )

        self._save_tasks(
            tasks
        )

        return task

    def list_tasks(
        self
    ):

        return (
            self._load_tasks()
        )

    def complete_task(
        self,
        task_id
    ):

        tasks = (
            self._load_tasks()
        )

        for task in tasks:

            if (
                task["id"] ==
                task_id
            ):

                task["status"] = (
                    "DONE"
                )

        self._save_tasks(
            tasks
        )

        return tasks

    def get_dashboard(
        self
    ):

        tasks = (
            self._load_tasks()
        )

        total_tasks = (
            len(tasks)
        )

        completed_tasks = (
            len(
                [
                    task
                    for task in tasks
                    if task["status"]
                    == "DONE"
                ]
            )
        )

        pending_tasks = (
            total_tasks -
            completed_tasks
        )

        completion_rate = 0

        if total_tasks > 0:

            completion_rate = round(
                (
                    completed_tasks /
                    total_tasks
                ) * 100,
                2
            )

        return {
            "total_tasks":
                total_tasks,

            "pending_tasks":
                pending_tasks,

            "completed_tasks":
                completed_tasks,

            "completion_rate":
                completion_rate
        }

    def get_analytics(self):
        tasks = self.list_tasks()

        total = len(tasks)

        completed = len([
            t for t in tasks
            if t["status"] == "DONE"
        ])

        pending = len([
            t for t in tasks
            if t["status"] == "PENDING"
        ])

        completion_rate = (
            round((completed / total) * 100, 2)
            if total > 0
            else 0
        )

        return {
            "total_tasks": total,
            "pending_tasks": pending,
            "completed_tasks": completed,
            "completion_rate": completion_rate
        }

    def get_upcoming_tasks(self):
        tasks = self.list_tasks()

        return [
            task
            for task in tasks
            if task["status"] == "PENDING"
        ]        