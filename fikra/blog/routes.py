from flask import (
render_template,
Blueprint,
)

#Add prefix
blog = Blueprint('blog', __name__, url_prefix='/blog')
    