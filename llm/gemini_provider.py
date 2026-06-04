from google import genai
from google.genai import types

from utils.settings import settings


class GeminiProvider:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = settings.GEMINI_MODEL

    def generate(
        self,
        prompt: str,
        temperature: float = 0.7
    ) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature
            )
        )

        if response.text:
            return response.text

        return "No response from Gemini."