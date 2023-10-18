from flask import Blueprint, render_template

app_routes = Blueprint("app_routes", __name__)


@app_routes.route("/")
def home():
    return render_template("home.html")
