from flask import render_template, redirect, url_for, request
from app.blueprints.main import main_blueprint


@main_blueprint.route("/")
def home():
    return render_template("home.html")
