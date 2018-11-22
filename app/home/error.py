from . import home
from flask import render_template


# 404
@home.app_errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404