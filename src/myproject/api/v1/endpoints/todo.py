from fastapi import APIRouter, HTTPException
from ....schemas.todo import TodoCreate, Todo, TodoUpdate
from ....crud.crud_todo import (
    create_todo,
    get_todos,
    get_todo,
    update_todo,
    delete_todo
)

router = APIRouter(prefix="/todo", tags=["todos"])

@router.post("/", response_model=Todo)
async def create_todo_api(todo: TodoCreate):
    return await create_todo(todo)

@router.get("/", response_model=list[Todo])
async def read_todos_api():
    return await get_todos()

@router.get("/{todo_id}", response_model=Todo)
async def read_todo_api(todo_id: str):
    todo = await get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=Todo)
async def update_todo_api(todo_id: str, todo: TodoUpdate):
    updated_todo = await update_todo(todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}")
async def delete_todo_api(todo_id: str):
    deleted = await delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
