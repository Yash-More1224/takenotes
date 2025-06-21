from pymongo import MongoClient

client = MongoClient('mongodb+srv://yashsmore7499:<db_password>@cluster0.hom9mcu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['takenotes']
collection = db['users']

# atlas project/cluster/db password:
# DaqunbmFErcXHS10 

# vs code connectoin string:
# mongodb+srv://yashsmore7499:DaqunbmFErcXHS10@cluster0.hom9mcu.mongodb.net/ 

# connevtion string for shell:
# mongosh "mongodb+srv://cluster0.hom9mcu.mongodb.net/" --apiVersion 1 --username yashsmore7499 --password DaqunbmFErcXHS10

# python connectoin string:
# mongodb+srv://yashsmore7499:<db_password>@cluster0.hom9mcu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

