from flask import Blueprint
from utils.functions import *

actorsBP = Blueprint("actors", __name__)
filePath = "app/files/actors.json"

@actorsBP.get("/")
def getActors():
    global filePath
    return readFile(filePath)

@actorsBP.get("/<int:id>")
def getSpecificActor(id):
    global filePath
    json = readFile(filePath)
    for actor in json:
        if actor["id"] == id:
            return actor, 200
    return {"error": "Actor not found."}, 404