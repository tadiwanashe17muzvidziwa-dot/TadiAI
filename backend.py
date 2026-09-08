# PRODUCTION SERVER — Used by Procfile
# This is the primary entry point for deployment (Railway/Render/Heroku)
# For local development, use main.py instead

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app.services.gemini import generate_response

# --- Pydantic Models -----------------------------------------------------------

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    history: list[dict[str, str]] = Field(default_factory=list)


class ChatResponse(BaseModel):
    response: str


# --- App Setup -----------------------------------------------------------------

app = FastAPI(title="TadiAI Backend", version="2.0.0")

# CORS — restrict in production via CORS_ORIGINS env var (comma-separated)
_origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in _origins if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates — serve the shared UI from Flask's template folder
TEMPLATES_DIR = Path(__file__).resolve().parent / "app" / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


# --- Routes --------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    try:
        result = generate_response(request.message, request.history)
        return ChatResponse(response=result)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        message = str(exc)
        if "429" in message or "RESOURCE_EXHAUSTED" in message:
            raise HTTPException(
                status_code=429,
                detail="AI usage limit reached. Please try again later.",
            ) from exc
        raise HTTPException(status_code=502, detail="Gemini could not respond.") from exc


# --- Entry Point ---------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
