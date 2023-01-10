from fastapi import FastAPI
from typing import List,AnyStr
from uuid import UUID ,uuid4
from models import User,Gender,Role

app = FastAPI()
#instance creation of application



db: List[User]=[
    User(
        id=uuid4(),
        first_name="Prudhvi",
        Last_name="Raj",
        gender=Gender.male,
        roles=[Role.admin]
    ),
     User(
        id=uuid4(),
        first_name="Anil",
        Last_name="Varma",
        gender=Gender.male,
        roles=[Role.student, Role.user]
    )
]
 
@app.get("/") #route for GET request & path
async def root():
    return{"hello":"Prudhvi"} #JSON object

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_users(user:User):
    db.append(user)
    return {"id": user.id}




