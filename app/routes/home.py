from flask import (Blueprint, render_template)
from ..shipping_form import ShippingForm

bp = Blueprint("home", __name__, url_prefix="")

@bp.route("/")
def packages():
    return render_template("base.html")

