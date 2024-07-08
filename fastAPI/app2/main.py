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


