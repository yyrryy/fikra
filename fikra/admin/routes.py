from crypt import methods
from flask import (
jsonify,
redirect,
render_template,
Blueprint,
request,
session,
url_for,
jsonify
)
from fikra.models import Users
from fikra.admin.funcs import admin_login
from fikra import bcrypt
#Add prefix
admin = Blueprint('admin', __name__, url_prefix='/admin')
    
@admin.route('/')
# @admin_login
def home():
    return render_template('admin/home.html')

@admin.route('/getin')
def getin():
    return render_template('admin/getin.html')

@admin.route('/login', methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    # check if username exists in db
    user = Users.query.filter_by(username=username).first()
    if user:
        # compare the hashed password with the password given
        if bcrypt.check_password_hash(user.password, password):
            
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for('admin.home'))
        # return json response for invalid password
        return jsonify({'success': False, 'message': 'Invalid password'})
    # return json response for invalid username
    return jsonify({'success': False, 'message': 'Invalid username'})





