import json
import os
from datetime import datetime

from models.automation_rule import AutomationRule


class AutomationManager:

    def __init__(self):

        self.file_path = "memory/automation_rules.json"

        if not os.path.exists(self.file_path):
            self._create_default_file()

    def _create_default_file(self):

        default_data = {
            "rules": []
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(default_data, file, indent=4)

    def load_rules(self):

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        rules = []

        for item in data.get("rules", []):

            rule = AutomationRule(
                name=item["name"],
                trigger_type=item["trigger_type"],
                condition=item["condition"],
                action=item["action"],
                enabled=item.get("enabled", True),
                execution_count=item.get("execution_count", 0),
                last_executed=item.get("last_executed")
            )

            rules.append(rule)

        return rules

    def save_rules(self, rules):

        data = {
            "rules": []
        }

        for rule in rules:

            data["rules"].append({
                "name": rule.name,
                "trigger_type": rule.trigger_type,
                "condition": rule.condition,
                "action": rule.action,
                "enabled": rule.enabled,
                "execution_count": rule.execution_count,
                "last_executed": rule.last_executed
            })

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_rule(
        self,
        name,
        trigger_type,
        condition,
        action
    ):

        rules = self.load_rules()

        rule = AutomationRule(
            name=name,
            trigger_type=trigger_type,
            condition=condition,
            action=action
        )

        rules.append(rule)

        self.save_rules(rules)

        return rule

    def list_rules(self):

        return self.load_rules()

    def run_rules(self):

        rules = self.load_rules()

        executed = 0

        for rule in rules:

            if not rule.enabled:
                continue

            self.execute_rule(rule)

            executed += 1

        self.save_rules(rules)

        return executed

    def execute_rule(self, rule):

        if not rule.enabled:
            return

        rule.execution_count += 1

        rule.last_executed = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def automation_dashboard(self):

        rules = self.load_rules()

        total_rules = len(rules)

        enabled_rules = len(
            [r for r in rules if r.enabled]
        )

        total_executions = sum(
            r.execution_count for r in rules
        )

        return {
            "total_rules": total_rules,
            "enabled_rules": enabled_rules,
            "total_executions": total_executions
        }