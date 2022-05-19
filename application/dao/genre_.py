from typing import Dict, Any

from marshmallow import ValidationError

from lib.dao import BaseDAO
from application.dao.models.models import Genre


class GenresDAO(BaseDAO):
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_id(self, mid):
        return self.session.query(Genre).get(mid)

    def update(self, mid: int, data: Dict[str, Any]):
        result = self.session.query(Genre).filter(Genre.id == mid).update(data)
        if result != 1:
            self.session.rollback()
            raise ValidationError(f"Movie with id {mid} not found")

        self.session.commit()

    def delete(self, mid: int):
        movie = self.session.query(Genre).filter(Genre.id == mid).first()
        self.session.delete(movie)
        self.session.commit()

    def create(self, data: Dict[str, Any]):

        new_movie = Genre(**data)
        self.session.add(new_movie)
        self.session.commit()

        return ""

