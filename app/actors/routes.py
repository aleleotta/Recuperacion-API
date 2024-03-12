from flask import Blueprint
from utils.functions import *

actorsBP = Blueprint("actors", __name__)

@actorsBP.get("/")
def getActors():
    pass