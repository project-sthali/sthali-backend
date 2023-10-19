"""Mapped methods for DB.
"""
from sthali_crud import Model, DB as Base


class DB(Base):
    """Sthali Backend DB main class.
    """
    # def create(self, resource: Model, *args, **kwargs) -> Model:
    #     breakpoint()
    #     return {'id': randint(1, 10), **resource}

    def read(self, resource_id: int, *args, **kwargs) -> Model:
        return {'id': resource_id, 'name': 'fernandes', 'height': 27}

    def upsert(self, resource_id: int, resource_obj: Model, *args, **kwargs) -> Model:
        return {**resource_obj, 'id': resource_id}

    # def delete(self, resource_id: int, *args, **kwargs) -> None:
    #     return None
