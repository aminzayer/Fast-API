from fastapi import FastAPI, HTTPException

app = FastAPI()

todos = []


@app.post("/todos/")
def create_todo(todo: str):
    todos.append(todo)
    return {"message": "Todo created successfully"}


@app.get("/todos/")
def get_todos():
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    deleted_todo = todos.pop(todo_id)
    return {"message": f"Todo '{deleted_todo}' deleted successfully"}
