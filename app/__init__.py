from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

from .routes import chat_api, page_routes


PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(page_routes)
    app.register_blueprint(chat_api)
    return app
