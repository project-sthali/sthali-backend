"""Mapped methods for DB.
"""
from typing import Any
from sthali_crud import DB as Base


class DB(Base):
    def create(self, resource: Any, *args, **kwargs) -> Any:
        return {**resource}

    def read(self, resource_id: int, *args, **kwargs) -> Any:
        return {'id': resource_id, 'name': 'fernandes', 'height': 27}

    def upsert(self, resource_id: int, resource_obj: Any, *args, **kwargs) -> Any:
        return {**resource_obj, 'id': resource_id}

    def delete(self, resource_id: int, *args, **kwargs) -> None:
        return None
