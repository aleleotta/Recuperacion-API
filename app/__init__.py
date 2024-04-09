from flask import *
from flask_jwt_extended import JWTManager, jwt_required
from utils.functions import *
from actors.routes import actorsBP
from films.routes import filmsBP
from users.routes import usersBP
import string
import secrets

app = Flask(__name__)

app.register_blueprint(actorsBP, url_prefix="/actors")
app.register_blueprint(filmsBP, url_prefix="/films")
app.register_blueprint(usersBP, url_prefix="/users")

alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for i in range(8))

app.config["SECRET_KEY"] = password
jwt = JWTManager(app)

@app.put("/backup")
@jwt_required
def backup():
    filmsBackupFilePath = "app/backups/films_backup.json"
    actorsBackupFilePath = "app/backups/actors_backup.json"
    filmsFilePath = "app/files/films_backup.json"
    actorsFilePath = "app/files/actors.json"
    films = readFile(filmsBackupFilePath)
    actors = readFile(actorsBackupFilePath)
    writeFile(filmsFilePath, films)
    writeFile(actorsFilePath, actors)
    return {"success": "Backups have been loaded."}, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)