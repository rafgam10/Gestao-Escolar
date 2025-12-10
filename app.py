from flask import Flask

from src.settings.config import Config
from src.settings.extensions import db
from src.settings.extensions import jwt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app=app)
jwt.init_app(app=app)

# Registrar as rotas:




if __name__ == "__main__":
    app.run(debug=True)