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
    # phone number is a string field length is 500
    phone = db.Column(db.String(500))
    # address is a string field length is 500
    address = db.Column(db.String(500))

    # referred by column will be one to many relationship witl users table
    referedby = db.Column(db.Integer, nullable=True)
    # referredby = db.relationship('Users', backref=db.backref('referedby', lazy='dynamic'))
    # is verified column will be boolean field
<<<<<<< HEAD
    # isverified = db.Column(db.Boolean, default=False)
    # REFRRALS COUNT
    #refcount = db.Column(db.Integer, default=0)
=======
    isverified = db.Column(db.Boolean, default=False)

>>>>>>> ac10b8cd0eccbc42ebfb0a902227c794801c1119


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
    date_posted=db.Column(db.DateTime.utcnow)
    
