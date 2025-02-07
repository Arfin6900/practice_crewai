from datetime import datetime
from bson import ObjectId
from ..core.database import todos_collection
from ..schemas.todo import TodoCreate, TodoUpdate

async def create_todo(todo: TodoCreate):
    todo_dict = todo.model_dump()
    todo_dict["created_at"] = datetime.utcnow()
    result = await todos_collection.insert_one(todo_dict)
    return {**todo_dict, "id": str(result.inserted_id)}

async def get_todos():
    todos = await todos_collection.find().to_list(1000)
    return [{**todo, "id": str(todo["_id"])} for todo in todos]

async def get_todo(todo_id: str):
    if not ObjectId.is_valid(todo_id):
        return None
    todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
    if todo:
        return {**todo, "id": str(todo["_id"])}
    return None

async def update_todo(todo_id: str, todo: TodoUpdate):
    if not ObjectId.is_valid(todo_id):
        return None
    update_data = todo.model_dump(exclude_unset=True)
    update_data["updated_at"] = datetime.utcnow()
    
    result = await todos_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": update_data}
    )
    
    if result.modified_count:
        return await get_todo(todo_id)
    return None

async def delete_todo(todo_id: str):
    if not ObjectId.is_valid(todo_id):
        return False
    result = await todos_collection.delete_one({"_id": ObjectId(todo_id)})
    return bool(result.deleted_count)
