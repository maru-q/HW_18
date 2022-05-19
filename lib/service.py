from typing import Dict, Any, TypeVar, Generic

from marshmallow import Schema

from lib.dao import BaseDAO

T = TypeVar("T", bound=BaseDAO)


class BaseService(Generic[T]):

    def __init__(self, dao: T, schema: Schema):
        self.dao = dao
        self.schema = schema

    def get_by_id(self, mid):
        return self.schema.dump(self.dao.get_by_id(mid))

    def get_all(self):
        return self.schema.dump(self.dao.get_all(), many=True)

    def create(self, data: Dict[str, Any]):
        return self.dao.create(self.schema.load(data))

    def delete(self, mid: int):
        return self.dao.delete(mid)

    def update(self, mid, data: Dict[str, Any]):
        self.dao.update(mid, self.schema.load(data))
