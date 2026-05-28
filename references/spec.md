# Todo API Spec

## 목표
FastAPI 기반 할 일 관리 REST API를 구현합니다.
저장소는 SQLite3를 사용합니다.

## 기능
각 기능은 commit 1개 단위로 구현합니다.

1. 할 일 추가 — `POST /todos`
2. 할 일 목록 조회 — `GET /todos`
3. 할 일 완료 처리 — `PATCH /todos/{id}`
4. 할 일 삭제 — `DELETE /todos/{id}`

## 데이터 모델
- `Todo`
  - `id`: `int`, Primary Key
  - `title`: `str`
  - `completed`: `bool`, default `false`

## API 계약

### 1. 할 일 추가
- Endpoint: `POST /todos`
- Request Body:
  ```json
  {
    "title": "Buy milk"
  }
  ```
- Response:
  - Status: `201 Created`
  - Body:
    ```json
    {
      "id": 1,
      "title": "Buy milk",
      "completed": false
    }
    ```

### 2. 할 일 목록 조회
- Endpoint: `GET /todos`
- Response:
  - Status: `200 OK`
  - Body:
    ```json
    [
      {
        "id": 1,
        "title": "Buy milk",
        "completed": false
      }
    ]
    ```

### 3. 할 일 완료 처리
- Endpoint: `PATCH /todos/{id}`
- 동작:
  - Request Body 없이 호출합니다.
  - 해당 Todo의 `completed` 값을 `true`로 변경합니다.
- Response:
  - Status: `200 OK`
  - Body:
    ```json
    {
      "id": 1,
      "title": "Buy milk",
      "completed": true
    }
    ```

### 4. 할 일 삭제
- Endpoint: `DELETE /todos/{id}`
- Response:
  - Status: `204 No Content`
  - Body 없음

## 에러 처리
- 존재하지 않는 `id`에 대해 `PATCH` 또는 `DELETE` 요청 시 `404 Not Found`를 반환합니다.
- `title`이 비어 있거나 공백만 포함하면 요청을 거부합니다.
- 잘못된 Request Body는 `422 Unprocessable Entity`를 반환합니다.

## 스택
- Python
- FastAPI
- SQLite3 (파일 기반, 예: `todos.db`)
- 테스트: `pytest`

## 테스트 요구사항
- TDD 필수 (테스트 먼저 작성)
- 테스트는 격리된 SQLite 환경(임시 파일 또는 `:memory:`)을 사용합니다.
- 각 endpoint에 대해 unit/integration 테스트를 작성합니다.
- 최소 포함 케이스:
  - `POST /todos` 성공
  - `GET /todos` 성공
  - `PATCH /todos/{id}` 성공
  - `DELETE /todos/{id}` 성공
  - 존재하지 않는 `id`에 대한 `PATCH / DELETE` 실패 (`404`)
  - 비어 있거나 공백인 `title` 요청 실패

## 비기능 요구사항
- 구현은 commit 1개 단위로 기능을 나눠 진행합니다.
- spec은 개발 시작 전 확정하고, 개발 중에는 변경하지 않습니다.
