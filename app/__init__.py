from flask import *
from actors.routes import actorsBP
from films.routes import filmsBP

app = Flask(__name__)

app.register_blueprint(actorsBP, url_prefix="/actors")
app.register_blueprint(filmsBP, url_prefix="/films")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)