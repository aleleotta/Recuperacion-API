from files import *
import json

def readFile(filePath):
    try:
        file = open(filePath, "r")
        list = json.load(file)
    except json.JSONDecodeError:
        list = []
    file.close()
    return list

def writeFile(filePath, data):
    file = open(filePath, "w")
    json.dump(data, file)
    file.close()

def findNextId(list: list):
    currentId = len(list)
    return currentId