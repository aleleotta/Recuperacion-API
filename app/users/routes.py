from flask import Blueprint, request
from bcrypt import *
from utils.functions import *

usersBP = Blueprint("users", __name__)
filepath = "app/files/users.json"

#region Endpoints
@usersBP.post("/")
def registerUser():
    if request.is_json:
        newUser = request.get_json()
        password = newUser["password"]
        salt = gensalt()
        hash = hashpw(password, salt)
#endregion