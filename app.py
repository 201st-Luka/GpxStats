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


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


#if __name__ == '__main__':

#Test Data
with app.app_context():
    app.run(debug=True)
    # db.init_app(app)
    db.create_all()

    user1 = Users(username='john_doe', email='noahbackes2@gmail.com', pwdHash='noahbknjhfdcthfccom')
    db.session.add(user1)
    db.session.commit()

    f1 = GPX_files(uid=user1.id)
    db.session.add(f1)
    db.session.commit()

    s1 = Stats(id=f1.id, uid=user1.id, length=1.5, duration=50.5, altitude=500.0, start_time=16.5, pace=4.51)
    db.session.add(s1)
    db.session.commit()



