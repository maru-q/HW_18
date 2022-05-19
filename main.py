from flask import Flask
from application.config import Config

from application.database import db
from flask_restx import Api

from application.fill_tables import load_data
from application.views.directors import director_ns
from application.views.genres import genre_ns
from application.views.movies import movie_ns
from application.fill_tables import data


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    return app


def configure_app(app: Flask):
    db.init_app(app)
    db.drop_all()
    db.create_all()
    load_data(data)
    api = Api(app, prefix="/api", doc="/docs")
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == "__main__":
    my_app = create_app()
    configure_app(my_app)
    my_app.run()
