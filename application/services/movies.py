from application.dao.movies import MoviesDAO
from lib.service import BaseService


class MoviesService(BaseService[MoviesDAO]):
    def get_by_director_id(self, director_id: int):
        return self.schema.dump(self.dao.get_by_director_id(director_id), many=True)

    def get_by_genre_id(self, genre_id: int):
        return self.schema.dump(self.dao.get_by_genre_id(genre_id), many=True)

    def get_by_year(self, year: int):
        return self.schema.dump(self.dao.get_by_year(year), many=True)

