from flask import render_template, redirect, url_for, request
from app.blueprints.tenants import tenants_blueprint
from app.models.tenants import Tenant


@tenants_blueprint.route("/", methods=["GET", "POST"])
def list_tenants():
    tenants_list = Tenant.query.all()
    return render_template("tenants/tenants.html", tenants=tenants_list)


@tenants_blueprint.route("/<int:tenant_id>", methods=["GET"])
def view_tenant(rental_id):
    rental = Tenant.query.get_or_404(rental_id)
    return render_template("tenants/tenant_details.html", rental=rental)
