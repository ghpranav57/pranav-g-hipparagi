from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import cgi

a_pi = FastAPI()


class info(BaseModel):
    name: str
    course_name: str
    join_date: str
    ph_no: str
    srn: str

@a_pi.get("/packet")
def stu_date():
    return "Student"

@a_pi.post("/send")
def create(name_var: info):
    name_encoded = jsonable_encoder(name_var)
    print(name_encoded)
    name = name_encoded["name"]
    print("Name: ",name)
    course_name = name_encoded["course_name"]
    print("course name: ",course_name)
    join_date = name_encoded["join_date"]
    print("join date: ",join_date)
    ph_no = name_encoded["ph_no"]
    srn = name_encoded["srn"]
    print("Phone number: ",ph_no)
    print("SRN: ",srn)
    return name,course_name,join_date,ph_no,srn

form = cgi.FieldStorage()
d = form.getvalue('stu_date')