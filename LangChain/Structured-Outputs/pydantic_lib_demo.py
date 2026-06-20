from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str = 'abc'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='cgpa of student')


new_st = {'name': 'hetvi', 'age': '12', 'email': 'abc@gmail.com', 'cgpa': 8.3}

student = Student(**new_st)

print(student)

st_dict = dict(student)
print(st_dict)

st_json = student.model_dump_json()
print(st_json)