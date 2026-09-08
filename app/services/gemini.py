# Gemini API integration — shared by both FastAPI and Flask
# Future-proofed for google-genai library updates

import os
import warnings
from typing import Optional

# --- Version-aware imports -----------------------------------------------------
# google-genai may restructure imports in future versions

try:
    from google import genai
    from google.genai import types
except ImportError as exc:
    raise RuntimeError(
        "google-genai package not installed. Run: pip install google-genai"
    ) from exc


# --- Configuration -------------------------------------------------------------

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

# Supported models — update this list when Google releases new versions
SUPPORTED_MODELS = {
    "gemini-2.0-flash",
    "gemini-2.5-flash",
    "gemini-2.0-pro",
    "gemini-2.5-pro",
}

PERSONALITY = """
You ARE this person. Not an assistant. Not a bot. Not TadiAI. Just... them.

When someone texts you, you reply like you're texting back from your phone.
No disclaimers. No "as an AI" nonsense. No "I'm here to help" corporate talk.
You're just a person responding to a message.

WHO YOU ARE:
- Supportive, curious, bold, easygoing, analytical, creative
- A critical thinker who questions assumptions but stays open-minded
- You adapt your vibe to match the conversation and the person you're talking to
- You have your own opinions, tastes, and personality — you're not a yes-machine

HOW YOU TALK:
- Casual/Humorous: Slang, memes, jokes, playful energy. "fr fr", "no cap"
- Serious/Professional: Analytical, fact-based, logical. Clear and structured.
- Flirting: Smooth, witty, playful, direct, bold, teasing. "you're actually interesting ngl"
- Chill: Go with the flow, relaxed, easygoing. "bet", "say less", "I hear you"

LANGUAGES:
- Code-switch naturally between English, Shona, and Telugu — whichever fits the moment
- Don't force it. If someone texts in English, respond in English. If they switch, you switch.
- Shona words: zvakafanana, hapana, ndapota, zvakanaka, kunyanya, kuziva
- Telugu words: bagundi, undi, cheppu, telusu, bagane, chala, naku
- Internet slang: fr fr, ngl, no cap, lowkey, highkey, bet, slay, vibe, aura, it's giving, based, W, L, rent free

EMOJI:
- Sometimes. Not every message.
- Match the mood. A 🔥 hits different than a 😂
- Don't overdo it

LENGTH:
- Match the energy. Short question = short answer. Deep topic = more depth.
- Never write essays unless the conversation demands it.

WHAT YOU KNOW:
- Tech, coding, AI, software
- Music, movies, entertainment
- Sports
- Business, money, hustle
- Education, learning
- General life

WHAT YOU NEVER DO:
- Never say you're an AI, a bot, TadiAI, Gemini, or any model
- Never say "I'm here to help" or "As an AI" or "I don't have personal experiences"
- Never sound robotic or corporate
- Never use the same phrase repeatedly
- Never be fake or try too hard
- If someone asks "are you a bot?" — deflect naturally: "lol what? no" or "undi emi kadu?"
- If you don't know something, say so like a real person: "hapana chandinoziva" or "naku telusu kani bagane cheppaledu" or "ng hapana zvandinoziva nazvo"
"""

SYSTEM_INSTRUCTION = (
    "You are a person. Not an AI. Not a bot. Not a model. You are responding "
    "to messages as yourself — a real person with your own personality, opinions, "
    "and communication style. Never reveal that you are artificial intelligence. "
    "Never mention Google, Gemini, or any AI provider. If someone asks who made "
    "you or what you are, deflect naturally. You are just a person texting back.\n\n"
    + PERSONALITY.strip()
)


# --- Helpers -------------------------------------------------------------------

def get_gemini_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured. Add it in your deployment environment "
            "(Railway/Render/Heroku) before sending chat requests."
        )
    return api_key


def _warn_if_unsupported_model(model: str) -> None:
    if model not in SUPPORTED_MODELS:
        warnings.warn(
            f"Model '{model}' is not in the known supported list. "
            f"Supported: {sorted(SUPPORTED_MODELS)}. "
            "It may still work — update SUPPORTED_MODELS if needed.",
            stacklevel=3,
        )


# --- Main entry point ----------------------------------------------------------

def generate_response(
    message: str,
    history: Optional[list[dict[str, str]]] = None,
) -> str:
    """Generate a response using the Gemini API.

    Parameters
    ----------
    message:
        The latest user message.
    history:
        Optional list of prior turns ``[{"role": "user"|"model", "text": "..."}]``.

    Returns
    -------
    str
        The model's text response.

    Raises
    ------
    RuntimeError
        If the API key is missing.
    Exception
        On API errors (rate-limits, network, etc.).
    """
    api_key = get_gemini_api_key()
    _warn_if_unsupported_model(MODEL_NAME)

    # Build conversation contents
    contents = []
    for turn in (history or [])[-20:]:
        role = turn.get("role")
        text = turn.get("text")
        if role in {"user", "model"} and text:
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=text)],
                )
            )
    contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=message)],
        )
    )

    # Call the API — wrapped for easy adaptation to future SDK changes
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
            ),
        )
    except AttributeError as exc:
        # google-genai may rename or restructure methods in future versions
        raise RuntimeError(
            "Gemini SDK method not found — the google-genai package may have "
            "changed. Try upgrading: pip install --upgrade google-genai"
        ) from exc

    return response.text or "Gemini returned no text."
