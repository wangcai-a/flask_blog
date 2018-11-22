from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint


app = Flask(__name__)
db = SQLAlchemy(app)


app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
