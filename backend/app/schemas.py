from pydantic import BaseModel

class TaskBase(BaseModel):
    owner: str

class TaskCreate(TaskBase):
    task_name: str

class TaskUpdate(BaseModel):
    task_name: str

class Task(TaskBase):
    id: int
    task_name: str
    
    class Config:
        orm_mode = True
