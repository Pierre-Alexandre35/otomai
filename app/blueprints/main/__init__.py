from flask import Blueprint

main_blueprint = Blueprint(
    "main", __name__, template_folder="templates", static_folder="static"
)

from . import routes  # Import routes after defining the blueprint
