from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from application.container import genres_service
from application.services.schemas.genre_ import GenreSchema

genre_ns = Namespace("genres")

genre_schema = GenreSchema()


@genre_ns.route("/<int:mid>")
class GenreView(Resource):

    def get(self, mid):
        return genres_service.get_by_id(mid), 200

    def put(self, mid: int):
        try:
            return genres_service.update(mid, request.json), 204
        except ValidationError as e:
            return {"errors": e.normalized_messages()}, 400

    def delete(self, mid):
        genres_service.delete(mid)

        return "", 204


@genre_ns.route("/")
class GenresView(Resource):

    def get(self):
        return genres_service.get_all(), 200

    def post(self):
        return genres_service.create(request.json), 201




