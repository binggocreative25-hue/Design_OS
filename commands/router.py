class CommandRouter:

    @staticmethod
    def is_command(
        brief: str,
        command: str
    ) -> bool:

        return brief.lower().startswith(
            command.lower()
        )