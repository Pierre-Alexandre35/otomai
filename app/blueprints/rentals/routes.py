from flask import render_template, redirect, url_for, request
from app.blueprints.rentals import rentals_blueprint
from app.models.rentals import Rental


@rentals_blueprint.route("/", methods=["GET", "POST"])
def list_rentals():
    rentals_list = Rental.query.all()
    return render_template("rentals/rentals.html", rentals=rentals_list)


@rentals_blueprint.route("/<int:rental_id>", methods=["GET"])
def view_rental(rental_id):
    rental = Rental.query.get_or_404(rental_id)
    return render_template("rentals/rental_details.html", rental=rental)
