from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    grade: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True