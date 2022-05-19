from sqlalchemy.orm import relationship

from application.dao.models.basemodel import BaseModel
from application.database import db


class Director(BaseModel):
    __tablename__ = "directors"

    name = db.Column(db.String)


class Genre(BaseModel):
    __tablename__ = "genres"

    name = db.Column(db.String())


class Movie(BaseModel):
    __tablename__ = "movies"

    title = db.Column(db.String(255))
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)

    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))

    director = relationship("Director")
    genre = relationship("Genre")


