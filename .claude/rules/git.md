# Git Workflow 규칙
## Repository shape
- 이 저장소는 monorepo다.
- 현재 작업 범위는 `backend/`만이며, `frontend/`는 구조만 유지한다.
- 공통 문서는 루트(`references/`, `.claude/`, `CLAUDE.md`)에 둔다.

## Branch
- main: 배포 가능 상태 (보호)
- dev: 통합 브랜치
- {type}/{description}: 작업 브랜치 (dev에서 분기 → dev로 merge)
- hotfix/{description}: 긴급 수정 (main에서 분기 → main+dev 반영)
- type: feat / fix / refactor / test / docs / chore
  예: feat/todo-create-endpoint, fix/todo-delete-404

## Commit (Conventional Commits)
형식: <type>(<scope>): <description>
- type: feat/fix/refactor/test/docs/chore (branch와 동일)
- scope는 가능하면 `backend` 또는 구체 기능명을 사용
- description: 명령형, 소문자 시작, 마침표 없음 ("add" not "added")
- 예: feat(backend): add todo create endpoint
- breaking change: feat!: ... 또는 footer에 BREAKING CHANGE:

## 원격 (GitHub)
- repo 생성과 연결은 Claude Code의 github MCP 단계에서 처리할 수 있다.
- 원격 연결 이후 각 commit 단위 완료 후 해당 브랜치를 push.
- 작업 완료 시 최종 push로 원격이 최신인지 확인.

## 운영
- 작업은 계획 단계에서 commit 단위로 분해 (기능 하나 = commit 하나, 각 단위에 branch 태그).
- 각 commit 단위 = TDD 한 사이클. 단위 완료마다 commit/push.
- push 전 테스트 통과 확인 (TDD green 상태).
