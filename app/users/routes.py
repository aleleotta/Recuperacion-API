from flask import Blueprint, request
from bcrypt import *
from utils.functions import *

usersBP = Blueprint("users", __name__)
filepath = "app/files/users.json"

#region Endpoints
@usersBP.post("/")
def registerUser():
    if request.is_json:
        userList = readFile(filepath)
        newUser = request.get_json()
        password = newUser["password"].encode("utf-8")
        salt = gensalt()
        hash = hashpw(password, salt).hex()
        newUser["password"] = hash
        userList.append(newUser)
        writeFile(userList, filepath)
        return newUser, 201
    else:
        return {"error": "The following request is not a JSON file."}, 415

#endregion