from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name" : "John",
        "age" : 17,
        "Year" : "year 17"
        }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class updateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(gt=0, lt=4)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student : Student):
    if student_id in student:
        return {"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/create-student/{student_id}")
def update_student(student_id: int, student: updateStudent):
    if student_id not in students:
        return{"Error" : "ID does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.year != None:
        students[student_id].year = student.year
    if student.age != None:
        students[student_id].age = student.age

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message" : " Student Deleted Successfully"}