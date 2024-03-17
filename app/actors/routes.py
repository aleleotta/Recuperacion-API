from flask import Blueprint, request
from utils.functions import *

actorsBP = Blueprint("actors", __name__)
filmsFilePath = "app/files/films.json"
actorsFilePath = "app/files/actors.json"

#region Endpoints
@actorsBP.get("/")
def getActors():
    global actorsFilePath
    return readFile(actorsFilePath)

@actorsBP.get("/<int:id>")
def getSpecificActor(id):
    global actorsFilePath
    actors = readFile(actorsFilePath)
    for actor in actors:
        if actor["id"] == id:
            return actor, 200
    return {"error": "The following actor was not found."}, 404

def findNextId(actors: list):
    currentId = actors.__len__ - 1
    return currentId

@actorsBP.post("/")
def createActor():
    if request.is_json:
        global actorsFilePath, filmsFilePath
        actors = readFile(actorsFilePath)
        films = readFile(filmsFilePath)
        actor = request.get_json()
        actor["id"] = findNextId(actors)
        for film in films:
            if film["id"] == actor["id_film"]:
                actors.append(actor)
                return actor, 201
        return {"error": "The film ID couldn't be identified so the following film wasn't posted into the list."}

def deleteActor(id):
    global actorsFilePath
    actors = readFile(actorsFilePath)
    for actor in actors:
        if actor["id"] == id:
            actorName = actor["actor_name"]
            actors.remove(actor)
            writeFile(actorsFilePath, actors)
            return {"message": f"The following actor was deleted: {actorName}"}, 200
    return {"error": "The following actor was not found."}, 404
#endregion