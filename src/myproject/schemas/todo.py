from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    title: Optional[str] = None
    completed: Optional[bool] = None

class Todo(TodoBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
