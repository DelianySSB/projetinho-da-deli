from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from os.path import dirname, abspath, exists
from os import remove as rmfile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

arquivobd = dirname(abspath(__file__))+"\\animais.db"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)