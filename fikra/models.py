from . import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(500))
    username= db.Column(db.String(500))
    email = db.Column(db.String(500))
    password = db.Column(db.String(500))
    # project colum is a string flield length is 500
    project = db.Column(db.String(500))
    rib = db.Column(db.String(500))
    referalcode= db.Column(db.String(500))
    # referred by column will be one to many relationship witl users table
    referedby = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    # referredby = db.relationship('Users', backref=db.backref('referedby', lazy='dynamic'))
    


# staff model
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    password = db.Column(db.String(500))
    email = db.Column(db.String(500))
    role = db.Column(db.String(500))


