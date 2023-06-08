from flask import (Blueprint, render_template)
from ..shipping_form import ShippingForm

bp = Blueprint("new_package", __name__, url_prefix="")

@bp.route("/new_package")
def new_package():
    form = ShippingForm()
    return render_template("shipping_request.html", form=form)
