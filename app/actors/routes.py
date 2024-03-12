from flask import Blueprint
from utils.functions import *

actorsBP = Blueprint("actors", __name__)
filePath = "app/files/actors.json"

@actorsBP.get("/")
def getActors():
    global filePath
    return readFile(filePath)