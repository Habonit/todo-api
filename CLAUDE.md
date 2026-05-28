# todo-api monorepo

이 저장소는 Todo API와 이후 React UI를 함께 관리하는 monorepo입니다.
구현 기준 문서는 루트 `references/spec.md`이며, 개발 중 spec을 수정하지 않습니다.

## Repository layout
- `backend/`: FastAPI + SQLite 기반 Todo API 구현 영역
- `frontend/`: React 기반 UI 영역 (나중에 구현)
- `references/`: 공통 frozen spec
- `.claude/rules/`: repo 공통 작업 규칙

## Current execution scope
- 지금 작업 대상은 `backend/`만입니다.
- `frontend/`는 구조만 두고 현재 구현하지 않습니다.

## Source of truth
- Spec: `references/spec.md`
- Rules: `@.claude/rules/tdd.md`, `@.claude/rules/git.md`

## Backend expectations
- Stack: Python, FastAPI, SQLite3, pytest, uv
- Package/deps management: `uv`
- `POST /todos`: title로 Todo 생성, `201 Created`
- `GET /todos`: 전체 Todo 목록 반환
- `PATCH /todos/{id}`: request body 없이 `completed=true` 처리
- `DELETE /todos/{id}`: `204 No Content`
- 없는 `id`: `404 Not Found`
- 빈/공백 `title` 또는 잘못된 body: 요청 거부

## Expected project shape
- `backend/app/`: API, models, persistence
- `backend/tests/`: unit / integration tests
- `backend/pyproject.toml`: backend package metadata
- `frontend/`: future React app
- `references/`: frozen spec copy

## Commands (backend)
- Create project metadata: `uv init backend --package`
- Create venv / sync deps: `cd backend && uv sync`
- Add runtime deps: `cd backend && uv add fastapi uvicorn`
- Add test deps: `cd backend && uv add --dev pytest httpx`
- Run backend tests: `cd backend && uv run pytest -q`
- Run backend app: `cd backend && uv run uvicorn app.main:app --reload`

## Non-negotiables
- TDD first: test -> fail -> implement -> pass -> refactor
- pytest only, not unittest
- Keep commits small: one feature per commit
- Stop and ask before risky actions (delete, force push, deploy)
- If implementation pressure conflicts with spec, stop and return to spec review
