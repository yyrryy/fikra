
from functools import wraps
from flask import (
    session,
    redirect,
    url_for
)

# login required function using flask session
def admin_login(views):
    @wraps(views)
    def wrapper(*args, **kwargs):
        if session['role'] == 'admin':
            return views(*args, **kwargs)
        else:
            return redirect(url_for('admin.login'))
    return wrapper

