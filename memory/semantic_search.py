from difflib import SequenceMatcher


class SemanticSearch:

    def similarity(
        self,
        a: str,
        b: str
    ) -> float:

        return SequenceMatcher(
            None,
            a.lower(),
            b.lower()
        ).ratio()

    def find_best_match(
        self,
        query: str,
        projects: list
    ):

        best_score = 0
        best_project = None

        for project in projects:

            brief = project[0]

            score = self.similarity(
                query,
                brief
            )

            if score > best_score:

                best_score = score
                best_project = project

        return best_project