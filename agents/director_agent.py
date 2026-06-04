import json

from llm.router import LLMRouter

from utils.language_manager import (
    LanguageManager
)

from models.director_output import (
    DirectorOutput
)


class DirectorAgent:

    def __init__(self):

        self.router = LLMRouter()

        self.language = LanguageManager()

    def analyze_brief(
        self,
        brief: str
    ) -> DirectorOutput:

        prompt = f"""
{self.language.get_system_prompt()}

Anda adalah Design Director AI.

Tugas:

Analisis kebutuhan proyek berikut.

Kembalikan JSON valid.

Format:

{{
    "project_type":"",
    "client_goal":"",
    "target_audience":"",
    "creative_direction":"",
    "workflow":"",
    "category":"",
    "tags":[]
}}

Workflow yang valid:

- PRICING
- VISUAL_CONCEPT
- PROPOSAL
- PROSPECTING
- REVISION
- SVG_LOGO

Aturan:

- Jika ada kata logo,
  branding,
  identitas merek,

  gunakan SVG_LOGO.

- category wajib berupa string.

Contoh:

branding
marketing
logo
social_media

- tags wajib berupa array.

Contoh:

[
    "logo",
    "branding",
    "coffee",
    "jakarta"
]

- Output HARUS JSON.

Kebutuhan proyek:

{brief}
"""

        response = self.router.generate(
            prompt=prompt,
            agent_name="DirectorAgent"
        )

        print("\n========== RAW RESPONSE ==========\n")
        print(response)
        print("\n==================================\n")

        response = response.strip()

        if response.startswith(
            "```json"
        ):
            response = (
                response
                .replace(
                    "```json",
                    ""
                )
                .replace(
                    "```",
                    ""
                )
                .strip()
            )

        if response == (
            "All AI providers failed."
        ):
            raise Exception(
                "Tidak ada provider AI yang tersedia."
            )

        try:

            data = json.loads(
                response
            )

        except Exception:

            raise Exception(
                f"""
AI tidak mengembalikan JSON valid.

Response:

{response}
"""
            )

        workflow = data.get(
            "workflow",
            ""
        )

        if isinstance(
            workflow,
            list
        ):
            workflow = workflow[-1]

        data["workflow"] = workflow

        #
        # PHASE 1I
        # PROJECT TAGS & CATEGORY
        #

        if "category" not in data:

            project_type = (
                data.get(
                    "project_type",
                    ""
                )
                .lower()
            )

            if "logo" in project_type:
                data["category"] = "branding"

            elif "branding" in project_type:
                data["category"] = "branding"

            elif (
                "marketing"
                in project_type
            ):
                data["category"] = "marketing"

            else:
                data["category"] = "general"

        if "tags" not in data:

            tags = []

            brief_words = (
                brief.lower()
                .replace(",", " ")
                .split()
            )

            for word in brief_words:

                if (
                    len(word) >= 4
                    and word not in tags
                ):
                    tags.append(
                        word
                    )

            data["tags"] = tags[:10]

        #
        # DirectorOutput
        # masih Phase 1H
        # jadi field tambahan
        # tidak dikirim ke model
        #

        return DirectorOutput(
    project_type=data[
        "project_type"
    ],
    client_goal=data[
        "client_goal"
    ],
    target_audience=data[
        "target_audience"
    ],
    creative_direction=data[
        "creative_direction"
    ],
    workflow=data[
        "workflow"
    ],
    category=data.get(
        "category",
        ""
    ),
    tags=data.get(
        "tags",
        []
    )
)