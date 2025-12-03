from flask import Blueprint, render_template, request

search_routes = Blueprint("search_routes", __name__)

@search_routes.route("/search/form")
@search_routes.route("/search")
def form():
    print("SEARCH FORM...")
    return render_template("search_form.html")
