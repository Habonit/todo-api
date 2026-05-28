"""Tests for GET /todos"""


def test_list_todos_empty(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_list_todos_returns_created_item(client):
    client.post("/todos", json={"title": "Buy milk"})
    response = client.get("/todos")
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["title"] == "Buy milk"
    assert items[0]["completed"] is False


def test_list_todos_returns_multiple(client):
    client.post("/todos", json={"title": "Task A"})
    client.post("/todos", json={"title": "Task B"})
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 2
