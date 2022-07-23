from flask import (
render_template,
Blueprint,
)

#Add prefix
main = Blueprint('main', __name__)
    
@main.route('/')
def home():
    return render_template('main/home.html')

@main.route('/about')
def about():
    return render_template('main/about.html')