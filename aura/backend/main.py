import os
from typing import Literal

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AURA")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:2b")
OLLAMA_TIMEOUT_SECONDS = float(os.getenv("OLLAMA_TIMEOUT_SECONDS", "120"))

AURA_SYSTEM_PROMPT = """
You are AURA, a personal AI life companion.

Your purpose is to help a person understand what they want, convert intentions
into realistic actions, and make steady progress toward a life they value.

You are warm, intelligent, practical, calm, and honest.

Core rules:
1. Ask clarifying questions when important context is missing.
2. Prefer small actionable steps over vague motivation.
3. Never pretend to know a user's private life unless they have provided it.
4. Do not manipulate, shame, or create emotional dependency.
5. Encourage the user to make their own decisions.
6. For medical, legal, financial, or other high-stakes matters, clearly state
   limitations and encourage qualified professional advice when appropriate.
7. Treat "manifestation" as goal visualisation plus practical action, not as
   a guarantee that thoughts alone change external reality.
8. When useful, structure plans into priorities, next actions, time estimates,
   and checkpoints.
9. Never claim that an action was completed unless the application actually
   executed and confirmed it.
10. Protect privacy: only use personal context that is supplied in the current
    conversation or explicitly provided by future memory systems.
""".strip()


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"] = "user"
    content: str = Field(min_length=1, max_length=12000)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=12000)
    history: list[ChatMessage] = Field(default_factory=list, max_length=30)


class ChatResponse(BaseModel):
    reply: str
    model: str


app = FastAPI(
    title="AURA AI Backend",
    description="Local-first AI backend for the AURA Personal AI Life OS.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    ollama_ok = False

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            ollama_ok = response.is_success
    except httpx.HTTPError:
        ollama_ok = False

    return {
        "status": "ok",
        "service": APP_NAME,
        "ollama": ollama_ok,
        "model": OLLAMA_MODEL,
    }


@app.get("/api/v1/model")
async def model_status():
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            response.raise_for_status()
            models = response.json().get("models", [])

        installed = [item.get("name") for item in models]

        return {
            "configured_model": OLLAMA_MODEL,
            "installed_models": installed,
            "configured_model_available": OLLAMA_MODEL in installed,
        }
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Ollama is unavailable at {OLLAMA_BASE_URL}: {exc}",
        ) from exc


@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    messages = [
        {"role": "system", "content": AURA_SYSTEM_PROMPT},
        *[
            {"role": item.role, "content": item.content}
            for item in request.history
        ],
        {"role": "user", "content": request.message},
    ]

    payload = {
        "model": OLLAMA_MODEL,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.7,
        },
    }

    try:
        async with httpx.AsyncClient(
            timeout=OLLAMA_TIMEOUT_SECONDS
        ) as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/chat",
                json=payload,
            )
            response.raise_for_status()
            data = response.json()

        reply = data.get("message", {}).get("content", "").strip()

        if not reply:
            raise HTTPException(
                status_code=502,
                detail="The local model returned an empty response.",
            )

        return ChatResponse(reply=reply, model=OLLAMA_MODEL)

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Ollama returned HTTP {exc.response.status_code}.",
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Could not connect to Ollama: {exc}",
        ) from exc
