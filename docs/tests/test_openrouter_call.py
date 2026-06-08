from llm.openrouter_provider import (
    OpenRouterProvider
)

provider = OpenRouterProvider()

response = provider.generate(
    "Say hello."
)

print(response)