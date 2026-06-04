import requests

r = requests.get(
    "https://openrouter.ai/api/v1/models"
)

data = r.json()

for model in data["data"]:
    model_id = model["id"]

    if ":free" in model_id:
        print(model_id)