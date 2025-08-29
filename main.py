# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Allow frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # during dev ok; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    done: bool = False

class Task(TaskCreate):
    id: int

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None

# In-memory store
tasks: List[Task] = []
task_counter = 1

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_counter
    new_task = Task(id=task_counter, **task.dict())
    tasks.append(new_task)
    task_counter += 1
    return new_task

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated: TaskCreate):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks[i] = Task(id=task_id, **updated.dict())
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")

# Partial update (toggle done)
@app.patch("/tasks/{task_id}", response_model=Task)
def patch_task(task_id: int, updated: TaskUpdate):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            current = t.dict()
            update_data = updated.dict(exclude_unset=True)
            current.update(update_data)
            tasks[i] = Task(**current)
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            return tasks.pop(i)
    raise HTTPException(status_code=404, detail="Task not found")
