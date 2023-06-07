from flask import Blueprint

bp = Blueprint("home", __name__, url_prefix="")

@bp.route("/")
def packages():
    return "<h1>Package Tracker</h1>"
