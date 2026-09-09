from fastapi.testclient import TestClient

from backend import app


client = TestClient(app)


def test_health_route():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_index_route():
    response = client.get("/")
    assert response.status_code == 200
    assert "TadiAI" in response.text


def test_chat_route_returns_response(monkeypatch):
    def fake_generate_response(message, history):
        assert message == "Hello"
        assert history == [{"role": "user", "text": "Hi"}]
        return "Hello there"

    monkeypatch.setattr("backend.generate_response", fake_generate_response)

    response = client.post(
        "/api/chat",
        json={"message": "Hello", "history": [{"role": "user", "text": "Hi"}]},
    )

    assert response.status_code == 200
    assert response.json() == {"response": "Hello there"}


def test_chat_route_rejects_empty_message():
    response = client.post("/api/chat", json={"message": ""})

    assert response.status_code == 422


def test_chat_route_reports_missing_configuration(monkeypatch):
    def missing_key(message, history):
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    monkeypatch.setattr("backend.generate_response", missing_key)

    response = client.post("/api/chat", json={"message": "Hello"})

    assert response.status_code == 500
    assert response.json() == {"detail": "GEMINI_API_KEY is not configured."}


def test_chat_route_maps_provider_errors(monkeypatch):
    def provider_failure(message, history):
        raise RuntimeError("provider failed")

    monkeypatch.setattr("backend.generate_response", provider_failure)

    response = client.post("/api/chat", json={"message": "Hello"})

    assert response.status_code == 500
    assert response.json() == {"detail": "provider failed"}


def test_chat_route_maps_rate_limit_errors(monkeypatch):
    def rate_limited(message, history):
        raise Exception("RESOURCE_EXHAUSTED")

    monkeypatch.setattr("backend.generate_response", rate_limited)

    response = client.post("/api/chat", json={"message": "Hello"})

    assert response.status_code == 429
    assert response.json() == {
        "detail": "AI usage limit reached. Please try again later."
    }
