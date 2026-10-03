from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from starlette import status


class TaskSchema(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

class TaskCreateSchema(BaseModel):
    title: str
    description: str = None
app = FastAPI()

task_list = [
    {
    "id": 1,
    "title": "Task 1",
    "description": "Task 1",
    "completed": False
    }
]

print ("hello")