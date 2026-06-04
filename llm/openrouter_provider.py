import requests

from utils.settings import settings


class OpenRouterProvider:

    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self):

        self.api_key = settings.OPENROUTER_API_KEY

    def generate(
        self,
        prompt: str,
        model: str = None
    ) -> str:

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model or settings.OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0
        }

        response = requests.post(
            self.BASE_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        if not response.ok:

            print("\n=== OPENROUTER DEBUG ===\n")
            print(response.status_code)
            print(response.text)
            print("\n========================\n")

            response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]
    