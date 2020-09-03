from sqlalchemy.orm import Session

from . import models, schemas


def create_school(db: Session, school_data: schemas.CreateSchool):
    school_data = models.School(school_name=school_data.school_name, address=school_data.address)
    db.add(school_data)
    db.commit()
    db.refresh(school_data)
    return school_data


def get_all_schools(db: Session):
    return db.query(models.School).all()


def get_school_by_id(db: Session, school_id: int):
    return db.query(models.School).filter(models.School.id == school_id).first()


def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).get(student_id)


def delete_school_by_id(db: Session, class_id: int):
    class_data = db.query(models.School).filter(models.School.id == class_id).first()
    db.delete(class_data)
    db.commit()


def delete_student_by_id(db: Session, student_id: int):
    student_data = db.query(models.Student).get(student_id)
    db.delete(student_data)
    db.commit()


def create_student(db: Session, student_data:schemas.CreateStudent):
    student_data = models.Student(first_name=student_data.first_name, last_name=student_data.last_name,
                                  address=student_data.address, school=student_data.school, email=student_data.email)
    db.add(student_data)
    db.commit()
    db.refresh(student_data)
    return student_data
