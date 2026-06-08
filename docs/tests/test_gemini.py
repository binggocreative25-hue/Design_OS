from llm.router import LLMRouter

router = LLMRouter()

response = router.generate(
    "Say hello from Design OS."
)

print(response)