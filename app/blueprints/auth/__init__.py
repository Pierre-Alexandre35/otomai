import os
from flask import Blueprint

auth_blueprint = Blueprint(
    "auth",
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../../templates/auth"),
    url_prefix="/auth",
)


from . import routes  # Import routes after defining the blueprint
