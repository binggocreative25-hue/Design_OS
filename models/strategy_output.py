from pydantic import BaseModel


class StrategyOutput(BaseModel):

    brand_personality: list[str]

    visual_direction: str

    logo_style: str

    color_palette: list[str]

    typography: list[str]

    moodboard_keywords: list[str]

    visual_prompt_en: str