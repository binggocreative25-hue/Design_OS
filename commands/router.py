class CommandRouter:

    @staticmethod
    def is_command(
        brief: str,
        command: str
    ) -> bool:

        return brief.lower().startswith(
            command.lower()
        )

    @staticmethod
    def extract_command_argument(
        brief: str,
        command: str
    ):

        if not CommandRouter.is_command(
            brief,
            command
        ):
            return None

        return (
            brief[
                len(command):
            ]
            .strip()
        )

    @staticmethod
    def is_score_client_command(
        brief: str
    ):

        return (
            CommandRouter.is_command(
                brief,
                "score client"
            )
        )

    @staticmethod
    def get_client_name_from_score_command(
        brief: str
    ):

        return (
            CommandRouter.extract_command_argument(
                brief,
                "score client"
            )
        )