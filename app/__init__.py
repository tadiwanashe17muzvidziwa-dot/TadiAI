from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from .routes import chat_api, page_routes


PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


def create_app() -> Flask:
    app = Flask(__name__)

    # CORS — restrict via CORS_ORIGINS env var (comma-separated) in production
    import os
    origins = os.getenv("CORS_ORIGINS", "*").split(",")
    CORS(app, origins=[o.strip() for o in origins if o.strip()])

    app.register_blueprint(page_routes)
    app.register_blueprint(chat_api)
    return app
