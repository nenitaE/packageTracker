from flask import Blueprint, render_template
from ..models import Package

bp = Blueprint("home", __name__, url_prefix="")

@bp.route("/")
def packages():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)
