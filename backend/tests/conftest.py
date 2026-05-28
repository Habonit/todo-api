import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import db


@pytest.fixture(autouse=True)
def reset_db():
    db.init_db(":memory:")
    yield
    db.close_db()


@pytest.fixture
def client(reset_db):
    return TestClient(app)
