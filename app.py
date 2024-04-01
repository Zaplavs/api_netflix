from flask import Flask
from movie.movie import movie_blueprint
from genre.genre import genre_blueprint
from rating.rating import rating_blueprint


app = Flask(__name__)

app.register_blueprint(movie_blueprint)
app.register_blueprint(genre_blueprint)
app.register_blueprint(rating_blueprint)

if __name__ == "__main__":
    app.run()