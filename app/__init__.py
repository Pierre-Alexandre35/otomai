from flask import Flask, render_template
from app.extensions import db, migrate
from app.blueprints.main import main_blueprint
from app.blueprints.rentals import rentals_blueprint


def create_app(config_class="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(rentals_blueprint)

    return app
