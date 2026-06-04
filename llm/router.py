import time

from rich.console import Console

from llm.gemini_provider import GeminiProvider
from llm.openrouter_provider import OpenRouterProvider

from memory.cache_manager import (
    CacheManager
)

from utils.ai_logger import (
    AILogger
)

console = Console()


class LLMRouter:

    def __init__(self):

        self.gemini = GeminiProvider()

        self.openrouter = OpenRouterProvider()

        self.cache = CacheManager()

        self.fallback_models = [

            "openai/gpt-oss-20b:free",

            "qwen/qwen3-next-80b-a3b-instruct:free",

            "meta-llama/llama-3.3-70b-instruct:free"

        ]

    def generate(
        self,
        prompt: str,
        agent_name: str = "Unknown"
    ) -> str:

        cached = self.cache.get(
            prompt
        )

        if cached:

            console.print(
                "[blue]CACHE HIT[/blue]"
            )

            AILogger.log(
                agent_name,
                "CACHE",
                "SUCCESS"
            )

            return cached[
                "response"
            ]

        try:

            console.print(
                "[green]Using Gemini[/green]"
            )

            response = (
                self.gemini.generate(
                    prompt
                )
            )

            self.cache.save(
                prompt,
                response
            )

            AILogger.log(
                agent_name,
                "Gemini",
                "SUCCESS"
            )

            return response

        except Exception as gemini_error:

            AILogger.log(
                agent_name,
                "Gemini",
                "FAILED"
            )

            console.print(
                f"[yellow]Gemini Failed:[/yellow] "
                f"{gemini_error}"
            )

        for model in self.fallback_models:

            try:

                console.print(
                    f"[cyan]Trying OpenRouter:[/cyan] "
                    f"{model}"
                )

                response = (
                    self.openrouter.generate(
                        prompt=prompt,
                        model=model
                    )
                )

                self.cache.save(
                    prompt,
                    response
                )

                AILogger.log(
                    agent_name,
                    model,
                    "SUCCESS"
                )

                return response

            except Exception as e:

                AILogger.log(
                    agent_name,
                    model,
                    "FAILED"
                )

                error_message = str(
                    e
                )

                console.print(
                    f"[red]Failed:[/red] "
                    f"{model}"
                )

                console.print(
                    error_message
                )

                if "429" in error_message:

                    console.print(
                        "[yellow]Rate limited. Waiting 15 seconds...[/yellow]"
                    )

                    time.sleep(
                        15
                    )

                continue

        return (
            "All AI providers failed."
        )