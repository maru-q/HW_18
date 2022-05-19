from marshmallow import Schema, fields, validates, ValidationError, validates_schema


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    director_id = fields.Int()
    genre_id = fields.Int()


    @validates_schema(pass_many=True)
    def root_validate(self, data, **kwargs):
        if data["title"] == "test":
            raise ValidationError("Title cannot be 'test'")
        return data

    @validates("year")
    def validate_year(self, value):
        if value < 1600:
            raise ValidationError("Year must be greater then 1600")
