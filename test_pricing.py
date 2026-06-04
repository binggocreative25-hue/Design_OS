from agents.pricing_agent import (
    PricingAgent
)

from utils.currency_formatter import (
    CurrencyFormatter
)

agent = PricingAgent()

result = agent.generate_price(
    project_type="Desain Logo",
    client_goal="Membangun citra premium",
    target_audience="Pasangan menengah atas"
)

print()

print("PAKET LOKAL")
print("-" * 40)

print(
    f"Basic    : "
    f"{CurrencyFormatter.idr(result.local_price['basic'])}"
)

print(
    f"Standard : "
    f"{CurrencyFormatter.idr(result.local_price['standard'])}"
)

print(
    f"Premium  : "
    f"{CurrencyFormatter.idr(result.local_price['premium'])}"
)

print()

print("PAKET INTERNASIONAL")
print("-" * 40)

print(
    f"Basic    : "
    f"{CurrencyFormatter.usd(result.international_price['basic'])}"
)

print(
    f"Standard : "
    f"{CurrencyFormatter.usd(result.international_price['standard'])}"
)

print(
    f"Premium  : "
    f"{CurrencyFormatter.usd(result.international_price['premium'])}"
)

print()

print(
    f"Segment           : {result.market_segment}"
)

print(
    f"Complexity Score  : {result.complexity_score}"
)

print(
    f"Recommended Pack  : {result.recommended_package}"
)

print()

print(
    f"Negotiation Floor : "
    f"{CurrencyFormatter.idr(result.negotiation_floor)}"
)

print(
    f"Target Price      : "
    f"{CurrencyFormatter.idr(result.target_price)}"
)

print(
    f"Ceiling Price     : "
    f"{CurrencyFormatter.idr(result.ceiling_price)}"
)