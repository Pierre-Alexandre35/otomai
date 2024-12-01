from flask import Flask, render_template, request, redirect, url_for
from app.extensions import db, migrate, login_manager
from app.blueprints.main import main_blueprint
from app.blueprints.rentals import rentals_blueprint
from app.blueprints.tenants import tenants_blueprint
from app.blueprints.auth import auth_blueprint
from flask_login import current_user


def create_app(config_class="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(rentals_blueprint)
    app.register_blueprint(tenants_blueprint)
    app.register_blueprint(auth_blueprint)

    login_manager.login_view = "auth.login"

    @app.before_request
    def require_login():
        # Skip authentication for login, register, and static files
        if not current_user.is_authenticated and request.endpoint not in [
            "auth.login",
            "auth.register",
            "static",
        ]:
            return redirect(url_for("auth.login"))

    return app


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()  # Rollback any failed database transactions
        return render_template("errors/500.html"), 500

    @app.errorhandler(403)
    def not_authorized(error):
        return render_template("errors/403.html"), 403
