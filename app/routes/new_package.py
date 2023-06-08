from flask import (Blueprint, render_template)
from ..shipping_form import ShippingForm

bp = Blueprint("new_package", __name__, url_prefix="")

@bp.route("/new_package")
def new_package():
    form = ShippingForm()
    ## The user pressed the "Submit" button
    # if form.submit.data:
    #     pass
    ## The user pressed the "Cancel" button
    # else:
    #     return render_template("base.html")
    return render_template("shipping_request.html", form=form)
