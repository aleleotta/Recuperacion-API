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
    actors = readFile(filePath)
    for actor in actors:
        if actor["id"] == id:
            return actor, 200
    return {"error": "The following actor was not found."}, 404

def deleteActor(id):
    global filePath
    actors = readFile(filePath)
    for actor in actors:
        if actor["id"] == id:
            actorName = actor["actor_name"]
            actors.remove(actor)
            writeFile(filePath, actors)
            return {"message": f"The following actor was deleted: {actorName}"}, 200
    return {"error": "The following actor was not found."}, 404