from flask import (
render_template,
Blueprint,
)

#Add prefix
main = Blueprint('main', __name__)
    
@main.route('/')
def home():
    return render_template('main/home.html')

@main.route('/getin')
def getin():
    return render_template('main/getin.html')