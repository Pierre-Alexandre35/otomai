import os
from flask import Blueprint

tenants_blueprint = Blueprint(
    "tenants",
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../../templates/tenants"),
    url_prefix="/tenants",
)


from . import routes  # Import routes after defining the blueprint
