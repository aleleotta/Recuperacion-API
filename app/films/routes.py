from flask import Blueprint
from utils.functions import *

filmsBP = Blueprint("films", __name__)
filePath = "app/files/films.json"

@filmsBP.get("/")
def getFilms():
    global filePath
    return readFile(filePath)