from pydantic import BaseModel, field_validator


class TodoCreate(BaseModel):
    title: str

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("title must not be blank")
        return v


class Todo(BaseModel):
    id: int
    title: str
    completed: bool
