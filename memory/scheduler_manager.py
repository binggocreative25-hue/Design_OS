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