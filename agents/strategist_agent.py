import json

from llm.router import LLMRouter

from models.strategy_output import (
    StrategyOutput
)

from utils.language_manager import (
    LanguageManager
)


class StrategistAgent:

    def __init__(self):

        self.router = LLMRouter()

        self.language = LanguageManager()

    def generate_strategy(
        self,
        project_type: str,
        client_goal: str,
        target_audience: str,
        creative_direction: str
    ):

        prompt = f"""
{self.language.get_system_prompt()}

Anda adalah Creative Director senior.

Tugas Anda adalah membuat strategi visual desain.

Kembalikan JSON valid.

Format:

{{
    "brand_personality": [],
    "visual_direction": "",
    "logo_style": "",
    "color_palette": [],
    "typography": [],
    "moodboard_keywords": [],
    "visual_prompt_en": ""
}}

Project Type:
{project_type}

Client Goal:
{client_goal}

Target Audience:
{target_audience}

Creative Direction:
{creative_direction}

Aturan:

- visual_prompt_en HARUS bahasa Inggris.
- Semua field lain HARUS bahasa Indonesia.
- color_palette berupa HEX.
- typography berupa nama font.
"""

        response = self.router.generate(
             prompt=prompt,
             agent_name="StrategistAgent"
        )

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

        data = json.loads(
            response
        )

        return StrategyOutput(
            **data
        )