from flask import Blueprint
from utils.functions import *

filmsBP = Blueprint("films", __name__)
filePath = "app/files/films.json"

@filmsBP.get("/")
def getFilms():
    global filePath
    return readFile(filePath), 200

@filmsBP.get("/<int:id>")
def getSpecificFilm(id):
    global filePath
    json = readFile(filePath)
    for film in json:
        if film["id"] == id:
            return film, 200
    return {"error": "Film not found."}, 404