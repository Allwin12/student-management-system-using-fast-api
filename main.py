from typing import List

import uvicorn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from sql_app import models, schemas, crud
from sql_app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# school CRUD operations
@app.post("/school/", response_model=schemas.SchoolInfo)
def create_school(data: schemas.CreateSchool, db: Session = Depends(get_db)):
    class_data = crud.create_school(db, data)
    return class_data


@app.get("/school/")
def get_all_schools(db: Session = Depends(get_db)):
    schools = crud.get_all_schools(db)
    if schools:
        return {
            "schools": schools
        }
    else:
        raise HTTPException(status_code=400, detail="No class exists")


@app.get("/school/{id}", response_model=schemas.SchoolInfo)
def get_school_by_id(id: int, db: Session = Depends(get_db)):
    db_school = crud.get_school_by_id(db, id)
    return db_school


@app.delete("/school/{id}")
def delete_school_by_id(id: int, db: Session = Depends(get_db)):
    crud.delete_school_by_id(db, id)
    return {"message": "class deleted successfully!"}


@app.put("/school/{id}")
async def edit_school_by_id(id: int, item: schemas.CreateSchool, db: Session = Depends(get_db)):
    update_item_encoded = jsonable_encoder(item)
    db.query(models.School).filter(models.School.id == id).update(update_item_encoded)
    db.commit()
    return {"success"}


# student crud operations
@app.post("/student/", response_model=schemas.StudentInfo)
def add_student(data: schemas.CreateStudent, db: Session = Depends(get_db)):
    student_data = crud.create_student(db, data)
    return student_data


@app.get("/student/")
def get_all_student(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    if students:
        return {
            "students": students
        }
    else:
        raise HTTPException(status_code=400, detail="No class exists")


@app.get("/student/{id}", response_model=schemas.StudentInfo)
def get_student_by_id(id: int, db: Session = Depends(get_db)):
    student_data = crud.get_student_by_id(db, id)
    return student_data


@app.delete("/student/{id}")
def delete_student_by_id(id: int, db: Session = Depends(get_db)):
    crud.delete_student_by_id(db, id)
    return {"message": "class deleted successfully!"}


@app.put("/student/{id}")
async def edit_student_by_id(id: int, item: schemas.CreateStudent, db: Session = Depends(get_db)):
    update_item_encoded = jsonable_encoder(item)
    db.query(models.Student).filter(models.Student.id == id).update(update_item_encoded)
    db.commit()
    return {"success"}
