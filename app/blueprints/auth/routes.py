from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.blueprints.auth import auth_blueprint
from app.models.user import User
from app.extensions import db


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("main.home"))
        flash("Invalid email or password")
    return render_template("auth/login.html")


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if User.query.filter_by(email=email).first():
            flash("Email already registered.")
        else:
            user = User(email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful! Please log in.")
            return redirect(url_for("auth.login"))
    return render_template("auth/register.html")
