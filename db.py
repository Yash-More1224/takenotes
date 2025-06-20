from pymongo import MongoClient

client = MongoClient('mongodb:///localhost:27017')
db = client['notes']
collection = db['notes_collection']

