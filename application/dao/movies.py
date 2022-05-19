from typing import Dict, Any

from marshmallow import ValidationError

from lib.dao import BaseDAO
from application.dao.models.models import Movie


class MoviesDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_id(self, mid):
        return self.session.query(Movie).get(mid)

    def update(self, mid: int, data: Dict[str, Any]):
        result = self.session.query(Movie).filter(Movie.id == mid).update(data)
        if result != 1:
            self.session.rollback()
            raise ValidationError(f"Movie with id {mid} not found")

        self.session.commit()

    def delete(self, mid: int):
        movie = self.session.query(Movie).filter(Movie.id == mid).first()
        self.session.delete(movie)
        self.session.commit()

    def create(self, data: Dict[str, Any]):

        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

        return ""

    def get_by_director_id(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_by_genre_id(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year)
