import bcrypt
from flask import (
render_template,
Blueprint,
request,
session,
redirect,
url_for
)
from fikra.dashboard.funcs import chackusername, user_login, signup_user, checkusername
from fikra.models import Users
#Add prefix
dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@user_login
@dashboard.route('/')
def home():
    return render_template('dashboard/home.html')

@dashboard.route('/newuser')
def newuser():
    return render_template('dashboard/newuser.html')

@dashboard.route('/signup/ref=<refcode>')
@dashboard.route('/signup/')
def signup(refcode=None):
    fullname=request.form['fullname']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    who_refered=Users.query.filter_by(referalcode=refcode).first()

    signup_user(fullname, username, email, password, who_refered)

@dashboard.route('/getin')
def getin(refcode=None):
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        user=Users.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.pss, password):
                session.clear()
                session['username'] = user.username
                users_refered=Users.query.filter_by(referedby=user).all()
                return redirect(url_for('dashboard.home'), user=user, users_refered=users_refered)
        else:
            return render_template('dashboard/getin.html', message="ERROR")
    return render_template('dashboard/getin.html')

