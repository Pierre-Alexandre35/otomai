import os
from flask import Blueprint

rentals_blueprint = Blueprint(
    "rentals",
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../../templates/rentals"),
    url_prefix="/rentals",
)


from . import routes  # Import routes after defining the blueprint
