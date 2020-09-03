from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sql_app.database import Base


class School(Base):
    __tablename__ = "school_info"

    id = Column(Integer, primary_key=True, index=True)
    school_name = Column(String)
    address = Column(Text)


class Student(Base):
    __tablename__ = "student_info"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(Integer)
    last_name = Column(String)
    address = Column(String)
    school = Column(Integer, ForeignKey("school_info.id"))
    email = Column(String, unique=True, index=True)


