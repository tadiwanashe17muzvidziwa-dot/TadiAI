from flask import Blueprint, current_app, jsonify, render_template, request

from .services.gemini import generate_response


page_routes = Blueprint("pages", __name__)
chat_api = Blueprint("chat_api", __name__)


@page_routes.get("/")
def index():
    return render_template("index.html")


@chat_api.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    history = data.get("history", [])

    if not message:
        return jsonify({"error": "Enter a message first."}), 400
    if not isinstance(history, list):
        return jsonify({"error": "Conversation history must be a list."}), 400

    try:
        return jsonify({"response": generate_response(message, history)})
    except RuntimeError as error:
        current_app.logger.exception("Gemini configuration error")
        return jsonify({"error": str(error)}), 500
    except Exception as error:
        current_app.logger.exception("Gemini request failed")
        if "429" in str(error) or "RESOURCE_EXHAUSTED" in str(error):
            return jsonify({"error": "The AI usage limit has been reached. Please try again later or check your API plan."}), 429
        return jsonify({"error": "Gemini could not respond. Check the server logs."}), 502
