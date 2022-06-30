from flask import (
render_template,
Blueprint,
)

from fikra.admin.funcs import admin_login
#Add prefix
admin = Blueprint('admin', __name__, url_prefix='/admin')
    
@admin.route('/')
# @admin_login
def home():
    return render_template('admin/home.html')

@admin.route('/getin')
def getin():
    return render_template('admin/getin.html')