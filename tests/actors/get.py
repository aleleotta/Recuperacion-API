import json
import requests
baseURL = "http://localhost:5050/actors"
response = requests.get(baseURL)
actorsList = response.json()
print("---------------------------------------------------------------------------------------------")
print("\nList:")
i = 1
for actor in actorsList:
    print(f"\t{i}) {actor['actor_name']}\n")
    i = i + 1
print("---------------------------------------------------------------------------------------------")