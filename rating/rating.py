from flask import Blueprint
from function import get_rating

rating_blueprint = Blueprint("rating_blueprint", __name__, template_folder='templates')

@rating_blueprint.route("/rating/children")
def get_genre_child():
    return get_rating(('G', 'G'))

@rating_blueprint.route("/rating/family")
def get_genre_family():
    return get_rating(('G', 'RG', 'PG-13'))


@rating_blueprint.route("/rating/adult")
def get_genre_adult():
    return get_rating(('R', 'NC-17'))

