from flask import Flask, render_template
from app.blueprints.main import main_blueprint


def create_app(config_class="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(main_blueprint)

    # Error handlers

    return app
