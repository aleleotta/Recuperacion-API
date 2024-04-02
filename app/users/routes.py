from flask import Blueprint, request
from bcrypt import *
from flask_jwt_extended import create_access_token
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
    
@usersBP.get("/")
def loginUser():
    if request.is_json:
        users = readFile(filepath)
        user = request.get_json()
        username = user["username"]
        for currentUser in users:
            if currentUser["username"] == username:
                password = user["password"].encode("utf-8")
                salt = gensalt()
                hash = hashpw(password, salt).hex()
                if user["password"] == hash:
                    token = create_access_token(identity = username)
                    return {"token": token}, 200
                else:
                    {"error": "Access denied."}, 401
            else:
                {"error": "The following user was not found."}, 404
    else:
        return {"error": "The following request is not a JSON file."}, 415

#endregion