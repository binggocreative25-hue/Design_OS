from memory.scheduler_manager import (
    SchedulerManager
)

scheduler = (
    SchedulerManager()
)

scheduler.create_task(
    "Follow Up MFI",
    "2026-06-10"
)

print(
    scheduler.list_tasks()
)