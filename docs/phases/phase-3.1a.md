# Phase 3.1A Smart Fallback Router

Multi model fallback
Retry 429
Retry 503
Cooldown system

Files:
- llm/router.py
- llm/openrouter_provider.py
- .env ubah model OPENROUTER_MODEL=openai/gpt-oss-20b:free
- .env ubah model OPENROUTER_MODEL=qwen/qwen3-next-80b-a3b-instruct:free

Features:
- Multi model fallback

Test:
python test_openrouter_call.py

Result:
PASS

Tag:
phase-3.1A
(belum mulai connect repository github)