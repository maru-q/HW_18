from typing import Dict, Any


class BaseDAO:

    def get_by_id(self, mid):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def create(self, data: Dict[str, Any]):
        raise NotImplementedError

    def update(self, mid: int, data: Dict[str, Any]):
        raise NotImplementedError

    def delete(self, mid: int):
        raise NotImplementedError



# class DataBaseDAO(BaseDAO)
#     def __init__(self, session):
#         self.session = session
