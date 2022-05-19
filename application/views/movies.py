from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from application.container import movies_service
from application.services.schemas.movie import MovieSchema

movie_ns = Namespace("movies")

movie_schema = MovieSchema()


@movie_ns.route("/<int:mid>")
class MovieView(Resource):

    def get(self, mid):
        return movies_service.get_by_id(mid), 200

    def put(self, mid: int):
        try:
            return movies_service.update(mid, request.json), 204
        except ValidationError as e:
            return {"errors": e.normalized_messages()}, 400

    def delete(self, mid):
        movies_service.delete(mid)

        return "", 204


@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        args = request.args
        if "director_id" in args:
            return movies_service.get_by_director_id(args["director_id"])

        if "genre_id" in args:
            return movies_service.get_by_genre_id(args["genre_id"])

        if "year" in args:
            return movies_service.get_by_year(args["year"])

        return movies_service.get_all(), 200

    def post(self):
        return movies_service.create(request.json), 201




