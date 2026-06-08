from agents.strategist_agent import (
    StrategistAgent
)

agent = StrategistAgent()

result = agent.generate_strategy(
    project_type="Desain Logo",
    client_goal="Membangun identitas visual premium",
    target_audience="Pasangan menengah atas",
    creative_direction="Elegan dan mewah"
)

print(
    result.model_dump_json(
        indent=2
    )
)