from flask import Blueprint
from function import get_title_movie, get_year_between

movie_blueprint = Blueprint("movie_blueprint", __name__, template_folder='templates')

@movie_blueprint.route("/movie/<title>")
def get_title(title):
    return get_title_movie(title)

@movie_blueprint.route("/movie/<int:year1>/to/<int:year2>")
def get_year_movie(year1, year2):
    return get_year_between(year1,year2)
