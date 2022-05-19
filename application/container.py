from application.dao.director import DirectorsDAO
from application.dao.genre_ import GenresDAO
from application.dao.movies import MoviesDAO
from application.database import db
from application.services.director import DirectorsService
from application.services.genre_ import GenresService
from application.services.movies import MoviesService
from application.services.schemas.director import DirectorSchema
from application.services.schemas.genre_ import GenreSchema
from application.services.schemas.movie import MovieSchema

movie_schema = MovieSchema()
director_schema = DirectorSchema()
genre_schema = GenreSchema()

movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao, movie_schema)

genres_dao = GenresDAO(db.session)
genres_service = GenresService(genres_dao, genre_schema)

directors_dao = DirectorsDAO(db.session)
directors_service = DirectorsService(directors_dao, genre_schema)

