from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    task_name:str
    status:str

all_tasks = {}

@app.get("/ping")
def ping():
    return "pong"

@app.get("/tasks")
def get_tasks() -> dict:
    return all_tasks


@app.post("/tasks_post")
def create_task_with_body(data:Data):
    all_tasks[data.task_name] = data.status  # Store data in dictionary
    return {"message": f"Task '{data.task_name}' added successfully!"}

@app.post("/tasks")
def create_task(task_name: str, status: str) -> str:
    all_tasks[task_name] = status
    return f"{task_name}:{status} created successfully."
@app.get("/")
def home():
    return {"message": "Welcome to Zahid's Todo App!"}
    
