import pytest

from cybersec_classifier.config import Config
from cybersec_classifier.bart_mnli import BartMNLIClassifier
from cybersec_classifier.cybersec_mlp import MLPClassifier


@pytest.fixture
def client():
    from cybersec_classifier import create_app

    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_bart_mnli():
    Config.MODEL = "bart_mnli"
    from cybersec_classifier import create_app

    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_with_api_key(monkeypatch):
    """Client with API key authentication enabled"""
    # Temporarily set API key for testing
    monkeypatch.setenv("API_KEY", "test-api-key-123")

    # Reload config to pick up the new API key
    Config.API_KEY = "test-api-key-123"
    from cybersec_classifier import create_app

    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def mlp():
    yield MLPClassifier()


@pytest.fixture(scope="session")
def bart_mnli():
    yield BartMNLIClassifier()
