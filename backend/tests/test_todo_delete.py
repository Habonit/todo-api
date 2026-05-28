"""Tests for DELETE /todos/{id}"""


def test_delete_todo_returns_204(client):
    created = client.post("/todos", json={"title": "Clean desk"}).json()
    response = client.delete(f"/todos/{created['id']}")
    assert response.status_code == 204


def test_delete_todo_removes_item(client):
    created = client.post("/todos", json={"title": "Clean desk"}).json()
    client.delete(f"/todos/{created['id']}")
    todos = client.get("/todos").json()
    assert all(t["id"] != created["id"] for t in todos)


def test_delete_todo_not_found(client):
    response = client.delete("/todos/9999")
    assert response.status_code == 404


def test_delete_todo_no_body(client):
    created = client.post("/todos", json={"title": "Tidy up"}).json()
    response = client.delete(f"/todos/{created['id']}")
    assert response.content == b""
