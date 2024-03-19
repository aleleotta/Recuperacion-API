from flask import *
from utils.functions import *
from actors.routes import actorsBP
from films.routes import filmsBP

app = Flask(__name__)

app.register_blueprint(actorsBP, url_prefix="/actors")
app.register_blueprint(filmsBP, url_prefix="/films")

filmsFilePath = "app/files/films.json"
actorsFilePath = "app/files/actors.json"

@app.put("/backup")
def backup():
    films = readFile(filmsFilePath)
    actors = readFile(actorsFilePath)
    return {"success": "Backups have been loaded."}, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)