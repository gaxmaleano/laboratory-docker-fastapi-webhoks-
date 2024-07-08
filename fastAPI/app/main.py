from fastapi import FastAPI, HTTPException
from models.models import ModelName
from models.models import ModelFile
from tags.tags import Tags
from os import system

app = FastAPI()
app.title = 'Titulo'
app.version = '0.0.1'

@app.get('/', tags=[Tags.course])
def home():
    return "Hola actualizado"

@app.get('/getDir', tags=[Tags.test])
def getDir():
    return {"dir": dir(app)}

@app.get('/item/{item_id}', tags=[Tags.course])
async def readItem(item_id : int):
    return {'item': {item_id}}

@app.get("/users/me", tags=[Tags.test])
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}", tags=[Tags.test])
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/", tags=[Tags.test])
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}", tags=[Tags.test])
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}", tags=[Tags.test])
async def read_file(file_path: str):
    
    with open(f"./{file_path}") as file:
        data = file.read()
        
    return {
        "file_path": file_path,
        "data": data
    }