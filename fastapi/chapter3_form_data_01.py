from fastapi import FastAPI, Form
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
async def create_user(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}