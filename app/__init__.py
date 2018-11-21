from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint


app = Flask(__name__)
db = SQLAlchemy(app)
