from flask import render_template, redirect, url_for, request
from app.blueprints.main import main_blueprint
from flask_login import login_required


@main_blueprint.route("/")
@login_required
def home():
    return render_template("home.html")
