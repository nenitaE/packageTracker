from flask import Blueprint, render_template, redirect, url_for
from ..shipping_form import ShippingForm
from ..models import Package, db

bp = Blueprint("new_package", __name__, url_prefix="")

@bp.route("/new_package", methods=["GET", "POST"])
def new_package():

    form =ShippingForm()

# idk this is made up but cancel isnt working
    if form.data["cancel"]:
        return render_template("base.html")

    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data["sender_name"],
                    recipient=data["recipient_name"],
                    origin=data["origin"],
                    destination=data["destination"],
                    location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        # return render_template("base.html")
        return redirect(url_for("home.packages"))

    return render_template("shipping_request.html", form=form)
