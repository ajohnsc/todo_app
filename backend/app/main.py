import os
import time
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from . import models, schemas, crud, database
from .database import SessionLocal

DATABASE_URL = os.environ.get('DATABASE_URL', 'mysql://root:example@db/todo_app')

# Function to create the database engine
def get_engine():
    while True:
        try:
            engine = create_engine(DATABASE_URL)
            # Test the connection
            with engine.connect() as connection:
                return engine
        except OperationalError:
            print("Database is not yet available, waiting...")
            time.sleep(5)

engine = get_engine()
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/tasks", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip=skip, limit=limit)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    crud.delete_task(db, task_id)
    return {"ok": True}

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return crud.update_task(db=db, task_id=task_id, task=task)
