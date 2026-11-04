from sqlmodel import Field , SQLModel

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None
    course: str

class Instructor(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None
    year: str

class Parent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    SonDept: str
    age: int | None = None
    sonyear: str
