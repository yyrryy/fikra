from fikra import db
from models import Users
def chackusername(u):
    # check if username exists in db
    user = Users.query.filter_by(username=u).first()
    if user:
        return True
    return False