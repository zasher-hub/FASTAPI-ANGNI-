from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import Student, Instructor, Parent

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Welcome to STUDENT API tehe~"}

@app.get("/Student/{id}")
async def read_Student(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        S1 = session.get(Student, id)
        return {"message": S1}
    

@app.post("/Student")
async def root(Student  : Student):
    with Session(engine) as session:
        session.add(Student)
        session.commit()
        session.refresh(Student)

        return {"message": 'created'}

@app.get("/Instructor/{id}")
async def read_Instructor(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        i2 = session.get(Instructor, id)
        return {"message": i2}
    

@app.post("/Instructor")
async def root(Instructor  : Instructor):
    with Session(engine) as session:
        session.add(Instructor)
        session.commit()
        session.refresh(Instructor)

        return {"message": 'created'}

@app.get("/Parent/{id}")
async def read_Parent(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        p3 = session.get(Parent, id)
        return {"message": p3}
    

@app.post("/Parent")
async def root(Parent  : Parent):
    with Session(engine) as session:
        session.add(Parent)
        session.commit()
        session.refresh(Parent)

        return {"message": 'created'}