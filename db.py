from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False) #soll unique sein
    pwdHash = db.Column(db.String(250), nullable=False)
    gpx_file = db.relationship('GPX_files', backref='users', lazy=True)
    stats = db.relationship('Stats', backref='users', lazy=True)


class GPX_files(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    file = db.Column(db.LargeBinary, nullable=True)  # nullable=False
    stats = db.relationship('Stats', backref='gpx_files', lazy=True)


class Stats(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('gpx_files.id'), primary_key=True, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    altitude = db.Column(db.Float, nullable=False)
    start_time = db.Column(db.Float, nullable=False)
    pace = db.Column(db.Float, nullable=False)
    hf = db.Column(db.Float, nullable=True)
    #Type
