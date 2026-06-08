import requests

r = requests.get(
    "https://openrouter.ai/api/v1/models"
)

print(r.status_code)
print(r.text[:200])