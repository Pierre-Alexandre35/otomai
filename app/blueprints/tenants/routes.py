from flask import render_template, redirect, url_for, request, abort
from app.blueprints.tenants import tenants_blueprint
from app.models.tenants import Tenant
from flask_login import current_user


@tenants_blueprint.route("/", methods=["GET", "POST"])
def list_tenants():
    tenants_list = Tenant.query.filter_by(user_id=current_user.id).all()
    return render_template("tenants/tenants.html", tenants=tenants_list)


@tenants_blueprint.route("/<int:tenant_id>", methods=["GET"])
def view_tenant(tenant_id):
    # Fetch the tenant and ensure it belongs to the current user
    tenant = Tenant.query.filter_by(id=tenant_id, user_id=current_user.id).first()
    if not tenant:
        # Return a 403 Forbidden error if the tenant does not belong to the user
        abort(403)
    return render_template("tenants/tenant_details.html", tenant=tenant)
