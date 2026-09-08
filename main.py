# LOCAL DEVELOPMENT SERVER — Do not use in production
# For production, use backend.py (FastAPI) via Procfile
# Run with: python main.py

import os

from app import create_app


app = create_app()


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"
    port = int(os.getenv("PORT", "5000"))
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
