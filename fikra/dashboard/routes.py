
from flask import (
render_template,
Blueprint,
request,
session,
redirect,
url_for
)
from fikra import db, bcrypt
from fikra.dashboard.funcs import user_login, checkusername, checkemail, generatecode
from fikra.models import Users

from random import choice
#Add prefix
dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
@user_login
def home():
    userid=session['userid']
    user = Users.query.filter_by(id=userid).first()
    referals=Users.query.filter_by(referedby=userid).all()
    return render_template('dashboard/home.html', user=user, referals=referals)

@dashboard.route('/newuser')
def newuser():
    return render_template('dashboard/newuser.html')

@dashboard.route('/signup/ref=<refcode>', methods=['POST', 'GET'])
def signup(refcode):
    if request.method=='POST':
        fullname=request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password'])
        who_refered=Users.query.filter_by(referalcode=refcode).first()
        project=request.form['project']
        rib=request.form['rib']
        characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
        code = ''
        for i in range(0, 11):
            code += choice(characters)
        db.session.add(Users(fullname=fullname, username=username, email=email, password=password, referedby=who_refered.id, project=project, rib=rib, referalcode=code))
        db.session.commit()
        return redirect(url_for('dashboard.verification'))
    return render_template('dashboard/getin.html', refcode=refcode)

@dashboard.route('/getin', methods=['POST', 'GET'])
def getin():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        user=Users.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            print('user found')
            session.clear()
            session['username'] = user.username
            session['userid'] = user.id
            users_refered=Users.query.filter_by(referedby=user.id).all()
            return redirect(url_for('dashboard.home', userid=user.id))
        else:
            return render_template('dashboard/getin.html', message="ERROR")
    return render_template('dashboard/getin.html')


@dashboard.route('/verification')
def verification():
    return render_template('dashboard/verification.html')

# logout route
@dashboard.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('dashboard.getin'))