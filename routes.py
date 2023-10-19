from flask import Blueprint, redirect, render_template, request
from sqlalchemy import null
from models import db, User

app_routes = Blueprint("app_routes", __name__)


@app_routes.route("/")
def home():
    users = db.session.execute(db.select(User)).scalars()
    return render_template("home.html", users=users)


@app_routes.route("/users/<user_id>")
def user_profile(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar_one()
    return render_template("user_profile.html", user=user)


@app_routes.route("/users/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        user = User(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            image_url=request.form["image_url"],
        )
        user.image_url = user.image_url if user.image_url else None

        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template("add_user.html")


@app_routes.route("/users/<user_id>/edit", methods=["GET", "POST"])
def edit_profile_user(user_id):
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    if request.method == "POST":
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        user.image_url = request.form["image_url"]

        db.session.add(user)
        db.session.commit()
        return redirect(f"/users/{user.id}")

    return render_template("edit_profile.html", user=user)


@app_routes.route("/users/<user_id>/delete")
def delete_profile_user(user_id):
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()
    db.session.delete(user)
    db.session.commit()
    return redirect("/")
