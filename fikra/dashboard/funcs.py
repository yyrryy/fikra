from flask import (
    jsonify,
    session,
    redirect,
    url_for
)
from sqlalchemy import false
from fikra import db, bcrypt
from fikra.models import Users

from functools import wraps

from random import choice

# generate unique code for referal code using bcrypt 11 length
def generatecode():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    code = ''
    for i in range(0, 11):
        code += choice(characters)
    # check if code exists inn db
    if Users.query.filter_by(referalcode=code).first():
        generatecode()
    return code


# user login function
def user_login(views):
    @wraps(views)
    def wrapper(*args, **kwargs):
        if session.get('username') is not None:
            return views(*args, **kwargs)
        else:
            return redirect(url_for('dashboard.getin'))
    return wrapper


def checkusername(u):
    # check if username exists in db
    user = Users.query.filter_by(username=u).first()
    if user:
        return False
    return True

# check if email exists in db
def checkemail(e):
    user = Users.query.filter_by(email=e).first()
    if user:
        return False
    return True

# signup function
def signup_user(fullname, username, email, password, who_refered):
    # check if username exists in db
    if chackusername(username):
        # return json respone with error with jsonify
        return jsonify({'error': 'username already exists'})
    # check if email exists in db
    if checkemail(email):
        # return json respone with error with jsonify
        return jsonify({'error': 'email already exists'})
    # generate hashed password with bcrypt
    psw=bcrypt.generate_password_hash(password).decode('utf-8')
    code=generate_code()

    user = Users(fullname=fullname, username=username, email=email, password=psw, referalcod=code, referedby=who_refered)
    db.session.add(user)
    db.session.commit()
    return jsonify({'success': 'user created'})


# get all users   