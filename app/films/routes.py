from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from utils.functions import *

filmsBP = Blueprint("films", __name__)
filmsFilePath = "app/files/films.json"
actorsFilePath = "app/files/actors.json"

#region Endpoints
@filmsBP.get("/")
def getFilms():
    global filmsFilePath
    return readFile(filmsFilePath), 200

@filmsBP.get("/<int:id>")
def getSpecificFilm(id):
    global filmsFilePath
    films = readFile(filmsFilePath)
    for film in films:
        if film["id"] == id:
            return film, 200
    return {"error": "The following film wasn't not found."}, 404

# Will return the actors of a specific film
@filmsBP.get("/<int:id>/actors")
def getActorsFromFilm(id):
    global filmsFilePath, actorsFilePath
    films = readFile(filmsFilePath)
    actors = readFile(actorsFilePath)
    for film in films:
        if film["id"] == id:
            filmActors = []
            for actor in actors:
                if actor["id_film"] == id:
                    filmActors.append(actor)
            if len(filmActors) == 0:
                return {"error": "No actors found for this film."}, 404
            return filmActors, 200
    return {"error": "The following film wasn't not found."}, 404

@filmsBP.put("/<int:id>")
@jwt_required()
def modifyFilm(id):
    if request.is_json:
        global filmsFilePath
        newFilm = request.get_json()
        films = readFile(filmsFilePath)
        newFilm["id"] = findNextId(films)
        for film in films:
            if film["id"] == id:
                for element in newFilm:
                    film[element] = newFilm[element]
                writeFile(filmsFilePath, films)
                return film, 200
        films.append(newFilm)
        writeFile(filmsFilePath, films)
        return newFilm, 201
    return {"error": "The request must be JSON."}, 400
#endregion