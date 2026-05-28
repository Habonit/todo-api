"""Tests for POST /todos"""


def test_create_todo_returns_201(client):
    response = client.post("/todos", json={"title": "Buy milk"})
    assert response.status_code == 201


def test_create_todo_returns_body(client):
    response = client.post("/todos", json={"title": "Buy milk"})
    body = response.json()
    assert body["title"] == "Buy milk"
    assert body["completed"] is False
    assert isinstance(body["id"], int)


def test_create_todo_empty_title_rejected(client):
    response = client.post("/todos", json={"title": ""})
    assert response.status_code == 422


def test_create_todo_whitespace_title_rejected(client):
    response = client.post("/todos", json={"title": "   "})
    assert response.status_code == 422


def test_create_todo_missing_title_rejected(client):
    response = client.post("/todos", json={})
    assert response.status_code == 422
