from . import db
import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(500))
    username= db.Column(db.String(500))
    email = db.Column(db.String(500))
    phone = db.Column(db.String(500))
    password = db.Column(db.String(500))
    # project colum is a string flield length is 500
    project = db.Column(db.String(500), nullable=True)
    rib = db.Column(db.String(500), nullable=True)
    referalcode= db.Column(db.String(500))
    # phone number is a string field length is 500
    # address is a string field length is 500
    address = db.Column(db.String(500), nullable=True)

    # referred by column will be one to many relationship witl users table
    referedby = db.Column(db.Integer, nullable=True)
    # referredby = db.relationship('Users', backref=db.backref('referedby', lazy='dynamic'))
    # is verified column will be boolean field
    isverified = db.Column(db.Boolean, default=False)
    # referral count column will be integer field
    referralcount = db.Column(db.Integer, default=0)


 

# staff model
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    password = db.Column(db.String(500))
    email = db.Column(db.String(500))
    role = db.Column(db.String(500))


# posts model
class Posts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(500))
    # content is a text field
    content=db.Column(db.Text)
    date_posted=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
