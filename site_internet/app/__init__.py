from flask import Flask, jsonify, Response, json, make_response
from config import CONFIG
from flask_sqlalchemy import SQLAlchemy
import os


chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
static = os.path.join(chemin_actuel, "static")


app = Flask(__name__, template_folder=templates, static_folder=static)
app.config.from_object(CONFIG)
db = SQLAlchemy(app)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../VTM.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



from app import routes, models



