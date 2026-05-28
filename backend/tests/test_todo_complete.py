"""Tests for PATCH /todos/{id}"""


def test_complete_todo_returns_200(client):
    created = client.post("/todos", json={"title": "Study"}).json()
    response = client.patch(f"/todos/{created['id']}")
    assert response.status_code == 200


def test_complete_todo_sets_completed_true(client):
    created = client.post("/todos", json={"title": "Study"}).json()
    response = client.patch(f"/todos/{created['id']}")
    body = response.json()
    assert body["completed"] is True
    assert body["id"] == created["id"]
    assert body["title"] == "Study"


def test_complete_todo_not_found(client):
    response = client.patch("/todos/9999")
    assert response.status_code == 404


def test_complete_todo_persists(client):
    created = client.post("/todos", json={"title": "Exercise"}).json()
    client.patch(f"/todos/{created['id']}")
    todos = client.get("/todos").json()
    assert todos[0]["completed"] is True
