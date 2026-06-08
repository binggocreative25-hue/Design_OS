from models.sales_strategy import SalesStrategy

strategy = SalesStrategy(
    client_name="MFI",
    client_score=65,
    client_tier="SILVER",
    closing_probability=80,
    revenue_potential="HIGH",
    priority="A",
    estimated_revenue=7500000,
    recommended_actions=[
        "Prepare proposal"
    ],
    upsell_services=[
        "Packaging Design"
    ]
)

print(
    strategy.to_dict()
)