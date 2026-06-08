from dataclasses import dataclass
from typing import Optional


@dataclass
class AutomationRule:
    name: str
    trigger_type: str
    condition: str
    action: str

    enabled: bool = True

    execution_count: int = 0

    last_executed: Optional[str] = None