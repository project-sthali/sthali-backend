"""Mapped methods for DB.
"""
from sthali_crud import Model, DB as Base


class DB(Base):
    """DB
    """
    def create(self, resource: Model, *args, **kwargs) -> Model:
        return {'id': 0, 'name': 'fernandes', 'height': 27}

    def read(self, resource_id: int, *args, **kwargs) -> Model:
        return {'id': 0, 'name': 'fernandes', 'height': 27}

    def update(self, resource_id: int, resource: Model, *args, **kwargs) -> Model:
        return {}

    def upsert(self, resource_id: int, resource: Model, *args, **kwargs) -> Model:
        return {}

    def delete(self, resource_id: int, *args, **kwargs) -> None:
        return None
