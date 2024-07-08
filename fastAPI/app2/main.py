from fastapi import FastAPI, HTTPException
# from models.models import ModelName
from models.models import ModelInsert
from tags.tags import Tags
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from os import environ
import json



app = FastAPI()
app.title = environ.get('FAST_TAG')
app.version = '0.0.1'


mongoIP = environ.get('MONGO_IP')
mongoPort = environ.get('MONGO_PORT')

mongoClient = MongoClient(f"mongodb://{mongoIP}:{mongoPort}")




@app.get('/', tags=[Tags.mongodb])
def home():
    return "Hola DASDADaaa"

@app.get('/getDBS', tags=[Tags.mongodb])
def home():
    response = {
        "dbs" : mongoClient.list_database_names()
    }
    return response

@app.post('/something/', tags=[Tags.mongodb])
def postData(data: str, age: int):
    user = {"name": data, "age": age}
    
    db = mongoClient['users']
    col = db['users']
    
    result = col.insert_one(user)
    
    return {
        'id': str(result.inserted_id),
        'user' : {
            'name' : data,
            'age' : age
        }
    }

@app.get('/something/', tags=[Tags.mongodb])
def getData(data: str):
    user = {"name": data}
    
    db = mongoClient['users']
    col = db['users']
    
    result = col.find_one(user)
    
    response = {}
    for key in result.keys():    
        response[key] = str(result[key])
    # return {
    #     # 'dir': type(result.values()).__name__,
    #     'keys': result.values().keys()
    #     # 'value' : result.values()
    # }
    return response

@app.get('/something/{data}', tags=[Tags.mongodb])
def getData(data: str):
    user = {"name": data}
    
    db = mongoClient['users']
    col = db['users']
    
    result = col.find_one(user)
    
    response = {}
    for key in result.keys():    
        response[key] = str(result[key])
    # return {
    #     # 'dir': type(result.values()).__name__,
    #     'keys': result.values().keys()
    #     # 'value' : result.values()
    # }
    return response