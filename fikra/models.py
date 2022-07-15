from . import db

class Users(db.models):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(500))
    username= db.Column(db.String(500))
    email = db.Column(db.String(500))
    password = db.Column(db.String(500))
    
# staff model
class Staff(db.models):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    password = db.Column(db.String(500))
    email = db.Column(db.String(500))
    role = db.Column(db.String(500))


