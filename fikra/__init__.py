from flask import Flask, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# urlparse is a standard Python module that parses URLs.
from urllib.parse import urlparse
import os

# import and configure flask migration
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['abdelouaheddb']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy(app)
bcrypt  = Bcrypt(app)
# configure flask migration
migrate=Migrate(app, db)


from fikra.blog.routes import blog
from fikra.main.routes import main
from fikra.admin.routes import admin
from fikra.dashboard.routes import dashboard

app.register_blueprint(blog)
app.register_blueprint(main)
app.register_blueprint(admin)
app.register_blueprint(dashboard)


@app.route("/sitemap")
@app.route("/sitemap/")
@app.route("/sitemap.xml")
def sitemap():

    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc
    
    # Static routes with static content
    static_urls = list()
    
    # Dynamic routes with dynamic content
    dynamic_urls = []
    
    xml_sitemap = render_template("sitemap.xml", static_urls=static_urls, dynamic_urls=dynamic_urls, host_base=host_base)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response
 
        
