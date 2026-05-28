# todo-api

A monorepo containing a FastAPI + SQLite backend and a React + Vite frontend for a simple Todo application.

The Playwright E2E test has been validated against the running backend and frontend as described below.

---

## Monorepo structure

```
todo-api/
├── backend/          # FastAPI + SQLite Todo API (Python, uv)
│   ├── app/          # API routes, models, SQLite persistence
│   └── tests/        # pytest unit and integration tests
├── frontend/         # React + Vite UI
│   ├── src/          # React components and API client
│   ├── e2e/          # Playwright E2E tests
│   └── playwright.config.js
├── references/
│   └── spec.md       # Frozen API specification (do not edit)
└── .claude/rules/    # Workflow rules (TDD, git)
```

---

## Running the backend

Requirements: Python 3.11+, [uv](https://docs.astral.sh/uv/)

```bash
# Install dependencies
cd backend && uv sync

# Start the dev server (port 8000)
cd backend && uv run uvicorn app.main:app --reload

# Run unit/integration tests
cd backend && uv run pytest -q
```

---

## Running the frontend

Requirements: Node.js 18+

```bash
# Install dependencies
cd frontend && npm install

# Start the dev server (port 5173, proxies /todos → localhost:8000)
cd frontend && npm run dev

# Production build
cd frontend && npm run build
```

---

## Running tests

### Backend (pytest)

```bash
cd backend && uv run pytest -q
```

### E2E (Playwright)

The Playwright config (`frontend/playwright.config.js`) automatically starts both the backend (`uvicorn`) and the frontend (`vite`) before running the tests — no manual server startup needed.

```bash
cd frontend && npm run test:e2e
```

The single E2E scenario covers the full happy path against the real running app:
1. Add a todo via the input field
2. Verify it appears in the list
3. Click the complete toggle and verify the completed state
4. Delete the todo and verify it is removed

---

## API endpoints

| Method | Path           | Description              | Success status |
|--------|----------------|--------------------------|----------------|
| POST   | `/todos`        | Create a todo (`title`)  | 201 Created    |
| GET    | `/todos`        | List all todos           | 200 OK         |
| PATCH  | `/todos/{id}`   | Mark todo as complete    | 200 OK         |
| DELETE | `/todos/{id}`   | Delete a todo            | 204 No Content |

Requests with a missing, empty, or whitespace-only `title` are rejected (422). Referencing a non-existent `id` returns 404.

---

## Notes

- The spec at `references/spec.md` is the source of truth and is never modified during development.
- All backend tests use an isolated in-memory SQLite database via pytest fixtures.
- The E2E test uses a timestamp-based unique title to remain resilient to data left over from previous runs.
