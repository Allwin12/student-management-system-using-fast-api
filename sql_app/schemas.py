from typing import List
from pydantic import BaseModel


class CreateSchool(BaseModel):
    school_name: str
    address: str


class CreateStudent(BaseModel):
    first_name: str
    last_name: str
    address: str
    school: int
    email: str


class UserInfoBase(BaseModel):
    username: str
    fullname: str


class UserCreate(UserInfoBase):
    password: str


class UserInfo(UserInfoBase):
    id: int
    username: str
    fullname: str

    class Config:
        orm_mode = True


class SchoolInfo(CreateSchool):
    id: int
    school_name: str
    address: str

    class Config:
        orm_mode = True


class StudentInfo(CreateStudent):
    id: int

    class Config:
        orm_mode = True
