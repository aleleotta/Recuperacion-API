from files import *
import json

def readFile(filePath):
    file = open(filePath, "r")
    list = json.load(file)
    file.close()
    return list

def writeFile(filePath, data):
    file = open(filePath, "w")
    json.dump(data, file)
    file.close()