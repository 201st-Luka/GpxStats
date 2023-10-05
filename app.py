from flask import Flask
from db import db, Users, GPX_files, Stats

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


#if __name__ == '__main__':

#Test Data
with app.app_context():
    app.run(debug=True)
    db.init_app(app)
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



