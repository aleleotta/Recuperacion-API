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

@actorsBP.post("/")
@jwt_required()
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
                writeFile(actorsFilePath, actors)
                return actor, 201
        return {"error": "The film ID couldn't be identified so the following actor wasn't posted into the list."}, 404
    return {"error": "The following request is not a JSON file."}, 415

@actorsBP.delete("/<int:id>")
@jwt_required()
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