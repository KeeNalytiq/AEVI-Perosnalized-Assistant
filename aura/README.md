# AURA — Personal AI Life OS

AURA is an open-source personal AI companion designed to help people turn intentions into practical action.

## Vision

AURA combines conversational AI, personal memory, goals, planning, habits, and approved tool actions into one privacy-conscious personal assistant.

## Current MVP

- Local open-weight LLM through Ollama
- FastAPI AI backend
- Conversation endpoint
- AURA system personality
- Health/model status endpoint
- Environment-based model configuration
- Clean foundation for memory, goals, habits, planning, voice, and tools

## Local AI

The default development model is Qwen3.5 2B through Ollama.

Install Ollama from https://ollama.com/download and run:

```bash
ollama pull qwen3.5:2b
```

## Backend

```bash
cd aura/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload --port 8000
```

API docs:

http://127.0.0.1:8000/docs

## Test

```bash
curl http://127.0.0.1:8000/health
```

Then:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Help me plan tomorrow so I can make progress toward my goals."}'
```

## Product roadmap

1. AI conversation
2. Personal memory
3. Vision and goals
4. Daily planning
5. Habits and routines
6. Tool/action engine
7. Voice
8. Personal insights
9. Privacy and consent controls
10. Public deployment

## Principle

AURA should increase a person's agency, not replace it. AI suggestions remain suggestions unless the user explicitly authorizes an action.
