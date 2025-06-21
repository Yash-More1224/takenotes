from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.cors.middleware import CORSMiddleware

app = FastAPI()

app.add_Middleware(
    CORSMiddleware, 
    add_methods = ["*"],
    add_headers = ["*"],
    add_origins = ["*"],
); 

client = MongoClient['mongodb+srv://yashsmore7499:<db_password>@cluster0.hom9mcu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0']
db = client['takenotes']
collection = db['users']

class resModel(BaseModel):
    title: str
    content: str

@app.get("/")
async def root():
    return {"message": "at root, Welcome to FastAPI"}

@app.post("/save-notes")
async def save_notes(data: resModel):
    collection.insertOne({"title":data.title, "content":data.content})
    return {"message": "note saved sucessfully!"}

@app.get("/get-notes")
async def fetch_notes():
    all_notes = db.users.find()
    return {all_notes}
