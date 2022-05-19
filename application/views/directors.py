from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError

from application.container import directors_service
from application.services.schemas.director import DirectorSchema

director_ns = Namespace("directors")

director_schema = DirectorSchema()


@director_ns.route("/<int:mid>")
class DirectorView(Resource):

    def get(self, mid):
        return directors_service.get_by_id(mid), 200

    def put(self, mid: int):
        try:
            return directors_service.update(mid, request.json), 204
        except ValidationError as e:
            return {"errors": e.normalized_messages()}, 400

    def delete(self, mid):
        directors_service.delete(mid)

        return "", 204


@director_ns.route("/")
class DirectorsView(Resource):

    def get(self):

        return directors_service.get_all(), 200

    def post(self):
        return directors_service.create(request.json), 201




