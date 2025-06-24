from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_origins = ["*"],
); 

client = MongoClient('mongodb+srv://yashsmore7499:DaqunbmFErcXHS10@cluster0.hom9mcu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
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
    collection.insert_one({"title":data.title, "content":data.content})
    return {"message": "note saved sucessfully!"}

@app.get("/get-notes")
async def get_notes():
    all_notes = db.collection.find()
    return {all_notes}