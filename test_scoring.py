from memory.client_scoring import ClientScoring

scoring = ClientScoring()

result = scoring.calculate_score(
    "ABC COFFEE"
)

print(result.to_dict())