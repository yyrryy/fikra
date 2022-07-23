from flask import (
render_template,
Blueprint,
)

from fikra import db
from fikra.models import Posts
#Add prefix
blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.route('/')
def home():
    # get all posts from the database and add pagination
    posts = Posts.query.all()
    return render_template('blog/home.html')

    
@blog.route('/post/<int:post_id>')
def post(post_id):
    post = Posts.query.filter_by(id=post_id).first()
    return render_template('blog/post.html', post=post)
