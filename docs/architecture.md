Design_OS Architecture

main.py
│
├── agents/
│   ├── director_agent.py
│   ├── pricing_agent.py
│   ├── strategist_agent.py
|
├── commands/
│   ├── router.py
│   ├── __init__.py
│
├── config/
│   ├── market_rates.json
│   ├── pricing_rules.json
│   ├── service_catalog.json  
│
├── docs/
│   ├── phases/
│   ├── tests/
│   ├── architecture.md
│   ├── changelog.md
│   ├── decisions.md
│   ├── roadmap.md
│
├── llm/
│   ├── gemini_provider.py
│   ├── openrouter-provider.py
│   ├── router.py
│
├── logs/
│   ├── ai_calls.log
│
├── memory/
│   ├── database.py
│   ├── client_manager.py
│   ├── history_manager.py
│   ├── context_manager.py
│   ├── cache_manager.py
│   ├── semantic_search.py
│   ├── project_context.json
│   ├── service_recommendation.py
│   ├── crm_manager.py
│   ├── crm_pipeline.json
│   ├── sales_manager.py 
│   ├── scheduler_manager.py
│   ├── scheduler_tasks.json
│
├── models/
│   ├── director_output.py
│   ├── pricing_output.py
│   ├── project_context.py
│   ├── strategy_output.py
│   ├── service_recommendation.py
│   ├── client_pipeline.py
│   ├── client_score.py
│   ├── sales_strategy.py
│
├── tools/
│   ├── pricing_engine.py
│   
├── utils/
│   ├── ai_logger.py
│   ├── currency_formatter.py
│   ├── language_manager.py
│   ├── settings.py