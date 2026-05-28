from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from app import db
from app.models import Todo, TodoCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield
    db.close_db()


app = FastAPI(lifespan=lifespan)


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate):
    conn = db.get_conn()
    cur = conn.execute(
        "INSERT INTO todos (title, completed) VALUES (?, 0)",
        (payload.title,),
    )
    conn.commit()
    row = conn.execute(
        "SELECT id, title, completed FROM todos WHERE id = ?",
        (cur.lastrowid,),
    ).fetchone()
    return Todo(id=row["id"], title=row["title"], completed=bool(row["completed"]))


@app.get("/todos", response_model=list[Todo])
def list_todos():
    conn = db.get_conn()
    rows = conn.execute("SELECT id, title, completed FROM todos").fetchall()
    return [Todo(id=r["id"], title=r["title"], completed=bool(r["completed"])) for r in rows]


@app.patch("/todos/{todo_id}", response_model=Todo)
def complete_todo(todo_id: int):
    conn = db.get_conn()
    row = conn.execute("SELECT id FROM todos WHERE id = ?", (todo_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    conn.execute("UPDATE todos SET completed = 1 WHERE id = ?", (todo_id,))
    conn.commit()
    row = conn.execute(
        "SELECT id, title, completed FROM todos WHERE id = ?", (todo_id,)
    ).fetchone()
    return Todo(id=row["id"], title=row["title"], completed=bool(row["completed"]))


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    conn = db.get_conn()
    row = conn.execute("SELECT id FROM todos WHERE id = ?", (todo_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
