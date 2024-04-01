from flask import Blueprint
from function import get_genre

genre_blueprint = Blueprint("genre_blueprint", __name__, template_folder='templates')

@genre_blueprint.route("/genre/<genre>")
def get_genre_all(genre):
    return get_genre(genre)
