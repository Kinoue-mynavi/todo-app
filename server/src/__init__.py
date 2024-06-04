from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r'/api/*': {'origins': 'http://localhost:5173'}})

app.config.from_object("src.config")

db = SQLAlchemy(app)
ma = Marshmallow(app)

import src.views


