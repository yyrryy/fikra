from flask import (
render_template,
Blueprint,
)

#Add prefix
dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')
    
@dashboard.route('/')
def home():
    return render_template('dashboard/home.html')

@dashboard.route('/newuser')
def newuser():
    return render_template('dashboard/newuser.html')