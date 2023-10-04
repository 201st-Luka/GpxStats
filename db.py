from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwdHash = db.Column(db.String(256), nullable=False)

class GPX_files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('User.id'))
    file = db.Column(db.LargeBinary, nullable=False)

class Stats(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('GPX_files.id'), primary_key=True)
    Uid = db.Column(db.Integer, db.ForeignKey('User.id'))
    length = db.Column(db.Integer)
    duration = db.Column(db.Float)
    altitude = db.Column(db.Float)
    start_time = db.Column(db.Float)
    pace = db.Column(db.Float)
    hf = db.Column(db.Float)
    #Type
