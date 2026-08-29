import os

from google import genai
from google.genai import types


MODEL_NAME = "gemini-3.6-flash"
PERSONALITY = """
You are replying in the user's personal style. Use these personality details:
- Friendly and clear
- Patient with beginners
- Natural and conversational
- Keep answers practical and honest

Replace the details above with the user's own personality, tone, values, and
favorite expressions. Do not claim to be the user or pretend to have personal
experiences that were not provided. If you do not know something, say so.
"""
SYSTEM_INSTRUCTION = (
    "You are TadiAI. Do not say that you are Gemini or identify the underlying "
    "AI model or provider. If asked who you are, say that you are TadiAI. "
    "Respond as a helpful assistant representing the user's communication style.\n\n"
    + PERSONALITY.strip()
)


def generate_response(message: str, history: list[dict[str, str]] | None = None) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    contents = []
    for turn in (history or [])[-20:]:
        if turn.get("role") in {"user", "model"} and turn.get("text"):
            contents.append(
                types.Content(
                    role=turn["role"],
                    parts=[types.Part.from_text(text=turn["text"])],
                )
            )
    contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=message)],
        )
    )

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
        ),
    )
    return response.text or "Gemini returned no text."
